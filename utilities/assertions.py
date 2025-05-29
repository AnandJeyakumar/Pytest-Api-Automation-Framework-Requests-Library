import logging


def postPet_assertions(json_data, payload):
    assert json_data['category']['id'] == payload['category']['id'], "Category ID Mismatch"
    assert json_data['category']['name'] == payload['category']['name'], "Category Name Mismatch"
    assert json_data['photoUrls'] == payload['photoUrls'], "Photo URL Mismatch"



def responsebody_assertions(json_data, payload):
    assert json_data['category']['id'] == payload['category']['id'], "Category ID Mismatch"
    assert json_data['category']['name'] == payload['category']['name'], "Category Name Mismatch"
    assert json_data['photoUrls'] == payload['photoUrls'], "Photo URL Mismatch"
    assert json_data['name'] == payload['name'], "Name Mismatch"
    assert json_data['status'] == payload['status'], "Status Mismatch"
    assert json_data['tags'][0]['id'] == payload['tags'][0]['id'], "Name Mismatch"
    assert json_data['tags'][0]['name'] == payload['tags'][0]['name'], "Name Mismatch"


def update_responsebody_notequal_assertions(json_data,payload):
    assert json_data['category']['id'] != payload['category']['id'], "Category ID Mismatch"
    assert json_data['category']['name'] != payload['category']['name'], "Category Name Mismatch"
    assert json_data['photoUrls'] != payload['photoUrls'], "Photo URL Mismatch"
    assert json_data['name'] != payload['name'], "Name Mismatch"
    assert json_data['tags'][0]['id'] != payload['tags'][0]['id'], "Name Mismatch"
    assert json_data['tags'][0]['name'] != payload['tags'][0]['name'], "Name Mismatch"
    print("****************Not equal assertions passed*************")


def delete_responsebody_assertions(json_data):
    assert json_data['message'] == "Pet not found", "Message Mismatch"
    assert json_data['type'] == "error", "Type Mismatch"
    assert json_data['code'] == 1, "code Mismatch"
    print("****************delete assertions passed*************")



