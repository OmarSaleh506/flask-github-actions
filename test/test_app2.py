import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    rv = client.get('/')
    assert False, "This test should be implemented in the future"
