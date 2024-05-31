import requests

def test_root_endpoint():
    response = requests.get('http://localhost:8000')
    assert response.status_code == 200
    assert response.text == "Hello, this is a simple API!"

def test_data_endpoint():
    response = requests.get('http://localhost:8000/data')
    assert response.status_code == 200
    data = response.json()
    assert data == {"name": "John", "age": 30, "city": "New York"}

def test_status_endpoint():
    response = requests.get('http://localhost:8000/status')
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "OK"}

def test_undefined_endpoint():
    response = requests.get('http://localhost:8000/undefined')
    assert response.status_code == 404
    data = response.json()
    assert data == {"error": "Endpoint not found"}

if __name__ == '__main__':
    test_root_endpoint()
    print("Test if root endpoint returns correct content.: OK")
    test_data_endpoint()
    print("Test if data endpoint returns correct data.: OK")
    test_status_endpoint()
    print("Test if status endpoint returns correct status.: OK")
    test_undefined_endpoint()
    print("Test if undefined endpoint returns correct status.: OK")
