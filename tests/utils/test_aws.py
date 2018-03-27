import moto

from falcon_lambda.utils import aws


@moto.mock_sts
def test_arn_building():
    arn = aws.build_arn('sns', 'test_topic')
    assert arn == 'arn:aws:sns:us-east-1:123456789012:test_topic'
