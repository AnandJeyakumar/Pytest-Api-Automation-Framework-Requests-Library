from utilities import requests_helper
from utilities import assertions
from utilities.data_generator import generate_random_post_pet_payload,updatePet
import pytest



def test_create_new_pet():
    payload = generate_random_post_pet_payload()
    response = requests_helper.post(payload)
    json_data = response.json()
    assert response.status_code == 200, "Status code mismatch"
    assertions.postPet_assertions(json_data,payload)
    assertions.responsebody_assertions(json_data,payload)


def test_getPetByID(new_pet_id):
    pet_id, payload = new_pet_id
    response = requests_helper.get(str(pet_id))
    json_data = response.json()
    assert response.status_code == 200 , "Status code mismatch"
    assert json_data['id'] == pet_id, "Id is not matched"
    assert json_data['category']['id'] == payload['category']['id'], "Category ID Mismatch"
    assertions.responsebody_assertions(json_data,payload)
    print("pet id", pet_id)
    print("json data", json_data)

@pytest.mark.updatePet
def test_update_pet(new_pet_id):
    petID, payload = new_pet_id
    print("Before update id payload is ", payload)
    putPayload = updatePet(petID)
    print("updated id payload is ", putPayload)
    response = requests_helper.put(putPayload)
    assert response.status_code == 200
    json_data = response.json()
    assert payload['category']['id'] != json_data['category']['id'],"Category ID did not change"
    assertions.responsebody_assertions(json_data,putPayload)
    assertions.update_responsebody_notequal_assertions(json_data,payload)


def test_delete_pet(new_pet_id):
    pet_id, payload = new_pet_id
    response = requests_helper.delete(str(pet_id))
    json_data = response.json()
    assert response.status_code == 200, "Status code mismatch"
    print("The response data is", json_data)
    assert json_data['message'] == str(pet_id)
    get_response = requests_helper.get(str(pet_id))
    print(get_response.status_code)
    print("json is", get_response.json())
    get_json_data = get_response.json()
    assertions.delete_responsebody_assertions(get_json_data)
    assert get_response.status_code == 404, "status code mismatch"







