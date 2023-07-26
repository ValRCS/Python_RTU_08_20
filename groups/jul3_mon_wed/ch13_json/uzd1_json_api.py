import json
import requests
import time # small delay between requests
 
url = "https://world.openfoodfacts.org/api/v0/product/"
 
#product_codes = ['4002724000775','4752050998719','7318690173830']
product_codes = ['4002724000775']
 
products = []
 
for i in product_codes:
  product_url = url + i + ".json"
  response = requests.get(product_url)
  product_data = json.loads(response.text)
  # product_name = product_data['product']['product_name']
  product_name = product_data['product']['product_name']
  product = {
    'name' : product_data['product']['product_name'],
    'ingredients' : []
    }
  
 
  for j in product_data['product']['ingredients']:
    try:
       vegan = j['vegan']
    except:
        vegan = 'no info'   
    ingredient = {
       'name' : j['text'],
       'vegan' : vegan
        }
    product['ingredients'].append(ingredient)
    
  products.append(product)
    
 
with open("my_product_data.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4)

# TODO create functions with parameters for getting data from API and saving it to file
# also we would like to call it asynchronically so it is not blocking