import json
import requests
import time
 
# produkta nosaukumu, ražotāju un kaloriju(ogļhidrāti, tauki, proteini) informāciju
 
def get_prod_description(baseurl:str = 'https://world.openfoodfacts.org/api/v0/product/',
                         barcodes:list = None,
                         delay:int = 0.1) -> list:
    """
    Function description
    """
    all_prods = []
    for prod in barcodes:
        url = baseurl + str(prod) + '.json'
        response = requests.get(url).json()
        print(f"{url} Product: {response['product']['product_name']}")

        def get_manufacturer(response):
            if response["product"].get("sources","") != "":
                for i in response["product"].get("sources",""):
                    if i.get('manufacturer','n/z')!='n/z':
                        return i['manufacturer']
            else:
                return ''
            
        small_info = {
            'product_name': response["product"]["product_name"],
            'generic_name': response["product"].get("generic_name",''),
            'manufacturer': get_manufacturer(response),
            #'partyName': response["product"].get("sources_fields",'').get('org-gs1','').get('partyName',''),
            'carbohydrates_100g': response["product"]["nutriments"]["carbohydrates_100g"],
            'fat_100g': response["product"]["nutriments"]["fat_100g"],
            'proteins_100g': response["product"]["nutriments"]["proteins_100g"]
        }
 
        all_prods.append(small_info)
        time.sleep(delay)
    return all_prods
 
 
prod_descr = get_prod_description(barcodes = [4751019531011, 5449000131805, 5053990156009, 8076800195057])
 
with open("prod_descr.json", "w", encoding="utf-8") as f:
    json.dump(prod_descr, 
              f, 
              indent=4, 
              ensure_ascii=False)
    
# i could transform prod_descr to pandas dataframe and then to csv file
import pandas as pd
df = pd.DataFrame(prod_descr)
# missing keys will be filled with NaN
df.to_csv('prod_descr.csv', index=False)

# make it work, make it right, make it fast.