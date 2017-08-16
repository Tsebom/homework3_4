from urllib.parse import urlencode

AUTORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6148694
VERSION = '5.67'

param_autorize = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'scope': 'friends',
    'response_type': 'token',
    'v': VERSION
}

print('?'.join(
    (AUTORIZE_URL, urlencode(param_autorize))
))

