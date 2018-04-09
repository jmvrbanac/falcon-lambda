import logging
import traceback

from aws_xray_sdk.core import patch_all, xray_recorder
from aws_xray_sdk.core.models import http
from aws_xray_sdk.core.lambda_launcher import check_in_lambda

from botocore import client
from botocore.vendored.requests import sessions

import falcon

log = logging.getLogger(__name__)

manager = None


class Manager(object):
    def __init__(self, patch=True):
        self._recorder = xray_recorder
        self._in_lambda = check_in_lambda()
        self._segment = None

        # HACK(jmvrbanac): Make sure we can run a local server without
        # xray blowing up.
        if not self.in_lambda:
            self.begin_segment('request')

        if patch:
            patch_all()

    def current_subsegment(self):
        return self._recorder.current_subsegment()

    def begin_segment(self, *args, **kwargs):
        self._segment = self._recorder.begin_segment(*args, **kwargs)
        return self._segment

    def end_segment(self, *args, **kwargs):
        return self._recorder.end_segment(*args, **kwargs)

    def begin_subsegment(self, *args, **kwargs):
        return self._recorder.begin_subsegment(*args, **kwargs)

    def end_subsegment(self, *args, **kwargs):
        return self._recorder.end_subsegment(*args, **kwargs)

    @property
    def in_lambda(self):
        return self._in_lambda

    @classmethod
    def setup(cls, *args, **kwargs):
        # Eww...
        global manager
        if not manager:
            manager = cls(*args, **kwargs)

        return manager

class Middleware(object):
    def process_request(self, req, resp):
        subsegment = manager.begin_subsegment('ProcessRequest')
        subsegment.put_http_meta(http.URL, req.relative_uri)
        subsegment.put_http_meta(http.METHOD, req.method)
        req.context['xray_subsegment'] = subsegment

    def process_response(self, req, resp, resource, req_succeeded):
        code, *_ = resp.status.partition(' ')

        subsegment = req.context['xray_subsegment']
        subsegment.put_http_meta(http.STATUS, code)

        manager.end_subsegment()

        if not manager.in_lambda:
            manager.end_segment()


def subsegment(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            manager.begin_subsegment(name)
            ret = func(*args, **kwargs)
            manager.end_subsegment()
            return ret
        return wrapper
    return decorator


def error_handler(ex, req, resp, params):
    if isinstance(ex, falcon.HTTPError):
        raise

    log.exception('Error caught!')
    stack = traceback.extract_stack(limit=manager._recorder._max_trace_back)

    subsegment = manager.current_subsegment()
    subsegment.put_http_meta(http.STATUS, 500)
    subsegment.add_exception(ex, stack)

    raise falcon.HTTPInternalServerError()


def disable_xray_in_boto(patch=False):
    Manager.setup(patch=patch)

    sessions._xray_enabled = False
    client._xray_enabled = False
