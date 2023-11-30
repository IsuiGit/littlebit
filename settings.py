import json, string

def loadUsers():
    try:
        data = None
        with open('core/users.json', 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except Exception as e:
        print('settings.py loadUsers() exception at:\n', e)
        return None

def saveUsers(data: dict):
    try:
        with open('core/users.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception as e:
        print('settings.py saveUsers() exception at:\n', e)
        return None
