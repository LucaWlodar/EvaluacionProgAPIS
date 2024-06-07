import requests, webbrowser, os, json
h = 0
n = int(input('por favor ingrese la cantidad de posts (mayor que 0 y menor que 100) '))
d = 0
posteos_primos = []
posteos_restantes = []
if n > 0 and n < 100 and int:
    while True:
        url = (f'https://jsonplaceholder.typicode.com/todos/{h+1}')
        api = requests.get(url)
        text = api.json()
        print(text)
        h = h+1  
        
        if h == n:
            break
else:
    print('Por favor ingrese una cantidad entera que cumpla con los requisitos')
    
dict = json.loads(text)
print(dict)
def numprim(text):
    if (text[id]):
        posteos_primos.append(text)
    print(posteos_primos)
numprim(text)   