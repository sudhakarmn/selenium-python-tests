import requests
from utilities.logger import get_logger

logger = get_logger()

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = self.base_url + endpoint
        logger.info(f"GET: {url}")
        response = requests.get(url)
        logger.info(f"Response: {response.status_code} - {response.text}")
        return response

    def post(self, endpoint, data, headers=None):
        url = self.base_url + endpoint
        logger.info(f"POST: {url} - Payload: {data} - Headers: {headers}")
        response = requests.post(url, json=data, headers=headers)
        logger.info(f"Response: {response.status_code} - {response.text}")
        return response

    def put(self, endpoint, data, headers=None):
        url = self.base_url + endpoint
        logger.info(f"PUT: {url} - Payload: {data} - Headers: {headers}")
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = self.base_url + endpoint
        logger.info(f"DELETE: {url} - Headers: {headers}")
        response = requests.delete(url, headers=headers)
        return response
