import requests
import json

risposta = requests.get('http://adminadmin.challs.cyberchallenge.it/admin.php')
for page in risposta.history:
    print(page.text)