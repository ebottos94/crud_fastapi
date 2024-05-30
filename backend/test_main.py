from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)

lot = {
    "start_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "harvest_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "yield_value": 0,
}


def test_crud_api():
    response = client.post("/api/lot/", json=lot)
    assert response.status_code == 201
    id_list = []
    id_list.append(response.json()["id"])
    response = client.put(f"/api/lot/{id_list[0]}", json={"yield_value": 5})
    assert response.status_code == 200
    response = client.get(f"/api/lot/{id_list[0]}")
    assert response.status_code == 200
    assert response.json()["yield_value"] == 5
    response = client.post("/api/lot/", json=lot)
    id_list.append(response.json()["id"])
    response = client.get("/api/lot/")
    assert response.status_code == 200
    for i in id_list:
        response = client.delete(f"/api/lot/{i}")
        assert response.status_code == 200
        response = client.delete(f"/api/lot/{i}")
        assert response.status_code == 404
        response = client.get(f"/api/lot/{i}")
        assert response.status_code == 404
