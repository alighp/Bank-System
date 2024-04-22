import json

def load_admin_credentials(filename):
    try:
        with open(filename, 'r') as file:
            credentials = json.load(file)
    except FileNotFoundError:
        credentials = {"username": "", "password": ""}
    return credentials

def update(filename,credentials):
    with open(filename, 'w') as file:
            json.dump(credentials, file)
    return credentials