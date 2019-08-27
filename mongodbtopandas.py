import pandas as pd
from pymongo import MongoClient

client = MongoClient()
db = client.csvtomongodb
collection = db.karakter
data = pd.DataFrame(list(collection.find()))

print(collection.find())
print(list(collection.find()))
print(data)

