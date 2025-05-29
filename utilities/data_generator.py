from faker import Faker
import random
fake = Faker()
def generate_random_post_pet_payload():
    return {
  "id": random.randint(1000000000, 9999999999),
        "category": {
            "id": random.randint(1, 100),
            "name": fake.word()
        },
        "name": fake.first_name(),
        "photoUrls": [
            fake.image_url()
        ],
        "tags": [
            {
                "id": random.randint(1, 100),
                "name": fake.word()
            }
        ],
        "status": random.choice(["available", "pending", "sold"])
    }


def updatePet(petID):
    return {
  "id": petID,
        "category": {
            "id": random.randint(1, 100),
            "name": fake.word()
        },
        "name": fake.first_name(),
        "photoUrls": [
            fake.image_url()
        ],
        "tags": [
            {
                "id": random.randint(1, 100),
                "name": fake.word()
            }
        ],
        "status": random.choice(["available", "pending", "sold"])
    }