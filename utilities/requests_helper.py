import  requests
from config.config import BASE_URL

def get(endPoint):
    return requests.get(BASE_URL + endPoint)

def post(payload):
    return requests.post(BASE_URL, json =payload)

def put(payload):
    return requests.put(BASE_URL, json =payload)

def delete(endPoint):
    return requests.delete(BASE_URL + endPoint)



