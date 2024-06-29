# Runtime: Python 3.12
import os

def handler(event, context):
  testEnvVar = os.environ['TEST_VALUE']

  print(f'Env var: {testEnvVar}')
  print(event)

  response = {
    'msg': 'Hello, world!'
  }

  print(response)
  return response
