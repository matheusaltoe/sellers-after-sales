import pytest
from faker import Faker

fake = Faker(["pt-BR"])
 
@pytest.fixture(scope="function")
def customer():
    postcode = fake.postcode()
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
    }

