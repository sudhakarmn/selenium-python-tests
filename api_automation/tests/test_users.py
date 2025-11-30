def test_get_single_user(user_client):
    response = user_client.get("/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_create_user(user_client):
    payload = {
        "name": "sudha",
        "job": "QA"
    }
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = user_client.post("/users", payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["name"] == "sudha"
