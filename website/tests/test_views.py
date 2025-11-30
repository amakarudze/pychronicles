def test_homepage_view(client):
    response = client.get("/")
    assert response.status_code == 200
