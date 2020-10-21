import requests

try:
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)
    print(response.text)
    print(response.json())

    response.raise_for_status() # raise an exception for 400 or 500 code
    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.') 
