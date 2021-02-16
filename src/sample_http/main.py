import base64
import pprint as pp

from flask import escape


def sample_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    subject = request.args.get('subject', 'World')
    subject = escape(subject)

    return f'Hello, {subject}!'
