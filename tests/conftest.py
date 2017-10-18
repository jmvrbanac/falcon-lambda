import falcon
import pytest


class QuoteResource(object):
    def on_get(self, req, resp):
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

    def on_post(self, req, resp):
        resp.media = req.media


@pytest.fixture
def sample_app():
    api = falcon.API()
    api.add_route('/quote', QuoteResource())

    yield api
