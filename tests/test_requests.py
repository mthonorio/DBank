import requests
import os

TOKEN = os.getenv('TOKEN')
headers = {'Authorization': f'Token {TOKEN}'} # Substitua pelo token real

def test_get_users():
    response = requests.get('http://127.0.0.1:8000/api/v1/users/')
    assert response.status_code == 200

def test_get_user():
    response = requests.get('http://127.0.0.1:8000/api/v2/users/1/', headers=headers)
    assert response.status_code == 200


def test_create_user():
    data = {
        'username': 'test',
        'password': 'test',
        'email': 'test@example.com'
    }
    response = requests.post('http://127.0.0.1:8000/api/v1/users/', data=data)
    assert response.status_code == 201


def test_get_accounts():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounts/')
    assert response.status_code == 200


def test_get_account():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounts/1/')
    assert response.status_code == 200


def test_create_account():
    data = {
        'user': 1,
        'account_number': '1234567890',
        'agency': '0001',
        'balance': 0.00
    }
    response = requests.post('http://127.0.0.1:8000/api/v1/accounts/', data=data)
    assert response.status_code == 201

test_get_users()
test_get_user()