import requests, json

def Products(product):
    url= f'https://fakestoreapi.com/products/{product}'
    response = requests.get(url)
    if response.ok:
        api = response.json()
        Fakeinfo = {}
        Fakeinfo['title'] = api['title'] 
        Fakeinfo['price'] = api['price'] 
        Fakeinfo['description'] = api['description'] 
        Fakeinfo['image'] = api['image'] 
        return Fakeinfo
    else:
        return None
    
  