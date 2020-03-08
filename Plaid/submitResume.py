import requests

url = 'https://derp.derpyuitest.com/derp'

params = {'name': 'AK',
            'resume': 'https://github.com/AKloc/resume/blob/master/Resume%20-%20Andy%20Kloc.pdf',
}

headers = {'Content-type': 'application/json'}
response = requests.post(url, json=params, headers=headers)

print(response.text) #TEXT/HTML
print(response.status_code, response.reason) #HTTP