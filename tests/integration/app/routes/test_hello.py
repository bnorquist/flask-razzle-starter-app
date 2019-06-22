

def test_hello(test_client):
    resp = test_client.get('/api/hello')
