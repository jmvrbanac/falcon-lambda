import boto3

cache = {}


def get_account_id():
    if not cache.get('aws_account_id'):
        sts = boto3.client('sts')
        resp = sts.get_caller_identity()

        cache['aws_account_id'] = resp.get('Account')

    return cache.get('aws_account_id')


def get_default_region():
    if not cache.get('default_region'):
        cache['default_region'] = boto3.session.Session().region_name

    return cache.get('default_region')


def build_arn(service, name, account=None, region=None, type=None):
    region = region or get_default_region()
    account = account or get_account_id()

    if service == 'iam':
        return f'arn:aws:{service}::{account}:{type}/{name}'

    elif service == 'lambda':
        type = type or 'function'
        return f'arn:aws:{service}:{region}:{account}:{type}:{name}'

    else:
        return f'arn:aws:{service}:{region}:{account}:{name}'
