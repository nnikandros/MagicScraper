import pandas as pd
import requests
import bs4
import json


inclusiondict={"at_most":"<", "exactly": "", "at_least":">" }

def mysearch(colors,param, legal="pioneer" ):
    """Gives the url for scr
    colors can be:
    any combination of "W" , "B"  , "U", "G","R", "C" ("colorless")
    ---------
    param can be :
    "at_most" : at most these colors
    "exactly" : exactly these colors
    "at_least": at least these colors  (including these colors)
    --------
    default legality is pionner
    """
    return f"https://api.scryfall.com/cards/search?as=grid&order=name&q=color{inclusiondict[param]}%3D{colors}+legal%3A{legal}+%28rarity%3Ar+OR+rarity%3Am%29"
  
  
url = mysearch("WG","at_most")
resp = requests.get(url)
data = resp.json

#print(type(data))
for key, value in data.items():
    print(key)
    
    
names=[]
prices=[]
for count, value in enumerate(dictresp["data"]):
    names.append(dictresp["data"][count]["name"] )
    prices.append(dictresp["data"][count]["prices"]["tix"])    
    
searchdict={"name": names,
      "price_tix": prices}

df = pd.DataFrame(searchdict)
print(df)

dfwithoutNa=df.dropna().sort_values(by="price_tix", ascending=False)
