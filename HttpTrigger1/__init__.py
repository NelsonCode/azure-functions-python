import logging
import azure.functions as func
from requests import get
from os import getenv
from dotenv import load_dotenv


load_dotenv()

# HTTP TRIGGER FOR DOWNLOAD REPO OF GITHUB

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    url = "https://github.com/USER/REPOSITORY/archive/BRANCH.tar.gz"
    headers = {
        "Authorization": "token " + getenv("GITHUB_TOKEN")
    }
    response = get(url=url, headers=headers)
    return func.HttpResponse(response.content)