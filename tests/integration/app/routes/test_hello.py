def test_hello(test_client):
    resp = test_client.get("/api/hello?name=lebron")
    assert resp.status_code == 200
    assert resp.get_json() == {"name": "lebron"}
