import requests

risposta = requests.get('http://onbusinessdev.challs.cyberchallenge.it/message.php')

print(risposta.text)