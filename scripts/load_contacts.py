import json
import requests


HOST = 'http://127.0.0.1:8000'


def get_token(username: str, password: str) -> str:
    params = {
        'username': username,
        'password': password,
    }
    raw_response = requests.post(
        url=f'{HOST}/api/token/',
        data=params
    ).content.decode()
    response = json.loads(raw_response)
    return response['token']


def get_contacts(token: str) -> list:
    headers = {'Authorization': f'Token {token}', }
    response = requests.get(
        url=f'{HOST}/api/contacts/',
        headers=headers
    )
    raw_json = response.content.decode()
    return json.loads(raw_json)


def run():
    username = input('Enter username: ')
    password = input('Enter password: ')

    token = get_token(username, password)
    contacts = get_contacts(token)

    json_contact = json.dumps(contacts, indent=4)
    print(json_contact)


if __name__ == '__main__':
    run()

