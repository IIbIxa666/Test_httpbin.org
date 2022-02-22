import pytest
import requests

API_URL = "https://api-dev.plutoview.com"


def test_get_company_planets_cost_1c(aut):
    response = requests.get(url=f"{API_URL}/company/planets_cost",
                            headers={"Authorization": f"Bearer {aut}"})
    print(aut)
    print(response.json().get("plan"))
    assert response.status_code == 200


def test_get_company_sessions_2c(aut):
    response = requests.get(url=f"{API_URL}/company/sessions",
                            headers={"Authorization": f"Bearer {aut}"})
    assert response.status_code == 200


def test_get_planets_1(aut):
    response = requests.get(url=f"{API_URL}/planet",
                            headers={"Authorization": f"Bearer {aut}"})
    assert response.status_code == 200


def test_get_planet_planet_uuid_2(aut, uuid):
    response = requests.get(url=f"{API_URL}/planet/{uuid}",
                            headers={"Authorization": f"Bearer {aut}"})
    print(uuid)
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_start_3(aut, uuid):
    response = requests.post(url=f"{API_URL}/planet/{uuid}/start",
                             headers={"Authorization": f"Bearer {aut}"})
    print(response.json().get("status"))
    assert response.json().get("status") == "running"
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_Update_4(aut, uuid):
    response = requests.patch(url=f"{API_URL}/planet/{uuid}",
                              headers={"Authorization": f"Bearer {aut}"},
                              json={"name": "TestingDEL123"})
    print(response.json().get("name"))
    assert (response.json().get("name") == "TestingDEL123")
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_conect_5(aut, uuid):
    response = requests.get(url=f"{API_URL}/planet/{uuid}/connect",
                            headers={"Authorization": f"Bearer {aut}"})
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_getOne_6(aut, uuid):
    response = requests.get(url=f"{API_URL}/planet/{uuid}",
                            headers={"Authorization": f"Bearer {aut}"})
    print(response.json().get("status"))
    assert(response.json().get("status") == "running")
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_stop_7(aut, uuid):
    response = requests.post(url=f"{API_URL}/planet/{uuid}/stop",
                             headers={"Authorization": f"Bearer {aut}"})
    print(response.json().get("status"))
    assert (response.json().get("status") == "stopped")
    assert response.status_code == 200

def test_PATCH_planet_planet_uuid_del_8(aut, uuid):
    response = requests.delete(url=f"{API_URL}/planet/{uuid}",
                               headers={"Authorization": f"Bearer {aut}"})
    print(response.json().get("message"))
    assert (response.json().get("message") == f"delete planet with uuid {uuid}")
    assert response.status_code == 200

