import prance

from falcon.media.validators import jsonschema

_swagger_spec = None


def load(path):
    spec = prance.ResolvingParser(path).specification
    return apply(spec)


def get():
    return _swagger_spec


def apply(spec):
    global _swagger_spec
    _swagger_spec = spec
    return _swagger_spec


def find_schema(path, action, spec):
    path_spec = spec['paths'][path][action]
    param = next(
        (
            item for item in path_spec['parameters']
            if item.get('name') == 'body'
        ),
        None
    )
    return param['schema']


def validate(path, action, spec):
    schema = find_schema(path, action, spec)
    return jsonschema.validate(schema)
