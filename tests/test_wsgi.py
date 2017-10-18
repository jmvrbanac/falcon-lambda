from falcon_lambda import wsgi
from tests.samples import sample_event


def test_handle_post_event(sample_app):
    event = sample_event(
        '/quote',
        'POST',
        body='{"message": "testing123"}'
    )

    resp = wsgi.adapter(sample_app, event, None)

    assert resp['statusCode'] == '200'
    assert resp['body'] == '{"message": "testing123"}'
    assert resp['headers'] == {
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '25'
    }
