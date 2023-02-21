import requests
from utils import is_valid_uuid

API_URL = "http://httpbin.org"


def test_bearer():
    response = requests.get(url=f"{API_URL}/bearer",
                            headers={"Authorization": "Bearer token"})
    assert response.status_code == 200
    response_body = response.json()
    assert response_body.get("authenticated") == True


def test_get():
    response = requests.get(url=f"{API_URL}/get")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["headers"]["Host"] == "httpbin.org"


def test_get_ip():
    response = requests.get(url=f"{API_URL}/ip")
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body.get("origin")) == 13


def test_get_user_agent():
    response = requests.get(url=f"{API_URL}/user-agent")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["user-agent"] == "python-requests/2.28.2"


def test_get_json():
    response = requests.get(url=f"{API_URL}/json")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["slideshow"]["author"] == "Yours Truly"


def test_get_uuid():
    response = requests.get(url=f"{API_URL}/uuid")
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body.get("uuid")) == 36
    assert is_valid_uuid(response_body.get("uuid"))


def test_get_methods():
    response = requests.get('https://httpbin.org/status/200')
    assert response.status_code == 200
    response = requests.get('https://httpbin.org/status/400')
    assert response.status_code == 400
    response = requests.get('https://httpbin.org/status/500')
    assert response.status_code == 500
