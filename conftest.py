

import pytest
import requests

API_URL = "https://api-dev.plutoview.com"


@pytest.fixture(scope="session")
def aut():
    response = requests.post(url=f"{API_URL}/auth/sign_in",
                             headers={"Content-Type": "application/x-www-form-urlencoded"},
                             data={"username": "superadmin",
                                   "password": '!Zk.mA:.~?n"g5RA'})
    return response.json().get("access_token")


@pytest.fixture(scope="session")
def uuid(aut):
 response = requests.post(f"{API_URL}/planet",
  headers={
   "Authorization": f"Bearer {aut}",
  },
  json={
   "name": "test-runner-planet",
   "planet_class": "personal"
  }
 )

 return response.json().get("uuid")

