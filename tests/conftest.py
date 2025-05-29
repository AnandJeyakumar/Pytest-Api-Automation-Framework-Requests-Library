import pytest
from utilities.data_generator import generate_random_post_pet_payload
from utilities import requests_helper

@pytest.fixture(scope="module")
def new_pet_id():
    payload = generate_random_post_pet_payload()
    response = requests_helper.post(payload)
    assert response.status_code == 200
    json_data = response.json()
    return json_data['id'], payload


