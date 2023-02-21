import pytest
import requests

API_URL = "http://httpbin.org"


@pytest.fixture(scope="session")
def aut():
    response = requests.post(url=f"{API_URL}/basic-auth/user/password",
                             headers={"Content-Type": "application/x-www-form-urlencoded"},
                             data={"username": "user",
                                   "password": 'password'})
    return response.json().get("access_token")


@pytest.fixture(scope="session")
def uuid(aut):
 response = requests.post(f"{API_URL}/plan",
  headers={
   "Authorization": f"Bearer {aut}",
  },
  json={
   "class": "personal"
  }
 )

 return response.json().get("uuid")

