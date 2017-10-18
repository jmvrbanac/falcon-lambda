import falcon
import pytest

from falcon_lambda.validators import swagger
from tests import data

swagger.load(str(data.get_path('sample-swagger.yml')))
spec = swagger.get()


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

    @swagger.validate('/quote', 'post', spec)
    def on_post(self, req, resp):
        resp.media = req.media


@pytest.fixture
def sample_app():
    api = falcon.API()
    api.add_route('/quote', QuoteResource())

    yield api
