import moto
import pytest

from falcon_lambda.utils import aws


@pytest.mark.parametrize('kwargs,expected', [
    (
        {'service': 'sns', 'name': 'test_topic'},
        'arn:aws:sns:us-east-1:123456789012:test_topic'
    ),
    (
        {'service': 'iam', 'name': 'thing', 'type': 'role'},
        'arn:aws:iam::123456789012:role/thing'
    ),
    (
        {'service': 'lambda', 'name': 'thing'},
        'arn:aws:lambda:us-east-1:123456789012:function:thing'
    ),

])
@moto.mock_sts
def test_arn_building(kwargs, expected):
    arn = aws.build_arn(**kwargs)
    assert arn == expected
