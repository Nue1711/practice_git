import requests

base_url = 'http://httpbin.org'

def get_delay(seconds):
    endpoint = f'/delay/{seconds}'

    print(f'getting with {seconds} delay..')
    res = requests.get(base_url + endpoint)
    data = res.json()
    print(data)

get_delay(5)
print("Okay! All finished getting.")