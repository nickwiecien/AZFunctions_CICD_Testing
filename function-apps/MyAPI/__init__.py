import logging

import azure.functions as func
import requests
import openai


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    resp = requests.get('https://bing.com')
    status_code = resp.status_code

    return func.HttpResponse(f"Status code: {status_code}")