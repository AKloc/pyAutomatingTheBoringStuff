import requests

# {
#   "name": "Jane Applicant",
#   "email": "jane@hotmail.com",
#   "resume": "www.linktoresume.io",
#   "phone": "123-456-7890", // optional
#   "github": "github.com/jane", // optional
#   "twitter": "@jane", // optional
#   "website": "www.jane.com", // optional
#   "location": "San Francisco", // optional
#   "favorite_candy": "m&m’s", // optional
#   "superpower": "multilingual" // optional
# }

url = 'https://contact.plaid.com/jobs'
#url = 'https://derp.derpyuitest.com/derp'

params = {'name': 'Andy Kloc',
            'email': 'Andy.Kloc@gmail.com',
            'resume': 'https://github.com/AKloc/resume/blob/master/Resume%20-%20Andy%20Kloc.pdf',
            'phone': '716-713-1171',
            'github': 'https://github.com/AKloc',
            'location': 'Buffalo, NY',
            'favorite_candy': 'Fireballs',
            'superpower': 'According to my wife, just now, patience.'}

headers = {'Content-type': 'application/json'}
response = requests.post(url, json=params, headers=headers)

print(response.text) #TEXT/HTML
print(response.status_code, response.reason) #HTTP