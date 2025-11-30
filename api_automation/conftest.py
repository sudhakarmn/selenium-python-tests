import pytest
from utilities.read_config import get_config
from utilities.api_client import APIClient

@pytest.fixture()
def user_client():
    base_url = get_config("API", "base_url")
    return APIClient(base_url)

@pytest.fixture()
def product_client():
    product_url = get_config("API", "product_url")
    return APIClient(product_url)
