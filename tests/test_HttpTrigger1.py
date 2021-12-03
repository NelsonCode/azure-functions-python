import unittest

import azure.functions as func
from HttpTrigger1 import main


class TestFunction(unittest.TestCase):
    def test_HttpTrigger1(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/HttpTrigger1')

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.status_code, 200,
        )