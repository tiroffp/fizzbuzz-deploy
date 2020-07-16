import json

def fizzbuzz(n):
	"""
	Compute the correct response for a number based on the 'Fizzbuzz' protocl

	Parameters
	----------
	n: number, required
		number to compute 'Fizzbuzz' result for

	Output
	------
	String
		'Fizzbuzz' result
	"""
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def build_response(data):
	"""
	Build a valid response object based on the given data

	Parameters
	-----------
	data: dict, required
		Data to be sent via HTTP response
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

	Output
	------
	Dict
		Formatted lambda response
	"""
	return {
		'statusCode': '200',
		'body': json.dumps(data),
		'headers': {
			'Content-Type': 'application/json',
		},
	}

def lambda_handler(event, context):
    """Lambda call  handler

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

	return build_response(fizzbuzz(event.pathParameters.number))
