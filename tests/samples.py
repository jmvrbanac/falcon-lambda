def sample_event(path='/quote', method='GET', body='', headers=None):
    all_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'cache-control': 'no-cache',
        'Content-Type': 'application/json',
        'Host': 'gy415nuibc.execute-api.us-east-1.amazonaws.com',
        'X-Forwarded-For': '54.240.196.186, 54.182.214.83',
        'X-Forwarded-Port': '443',
        'X-Forwarded-Proto': 'https'
    }
    all_headers.update(headers or {})

    event = {
        'resource': '/{proxy+}',
        'path': path,
        'httpMethod': method,
        'headers': all_headers,
        'queryStringParameters': {
            'name': 'me'
        },
        'pathParameters': {
            'proxy': path.lstrip('/')
        },
        'stageVariables': {
            'stageVariableName': 'stageVariableValue'
        },
        'requestContext': {
            'accountId': '12345678912',
            'resourceId': 'roq9wj',
            'stage': 'testStage',
            'requestId': 'deef4878-7910-11e6-8f14-25afc3e9ae33',
            'identity': {
                'cognitoIdentityPoolId': None,
                'accountId': None,
                'cognitoIdentityId': None,
                'caller': None,
                'apiKey': None,
                'sourceIp': '192.168.196.186',
                'cognitoAuthenticationType': None,
                'cognitoAuthenticationProvider': None,
                'userArn': None,
                'userAgent': 'PostmanRuntime/2.4.5',
                'user': None
            },
            'resourcePath': '/{proxy+}',
            'httpMethod': method,
            'apiId': 'gy415nuibc'
        },
        'body': body,
        'isBase64Encoded': False
        }

    return event
