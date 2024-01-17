import pymongo

myclient = pymongo.MongoClient("mongodb://root:root@mongo:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)


database_names = myclient.list_database_names()

collection_names = mydb.list_collection_names()

print("Inserted id: ", x.inserted_id)

print("Databases: " + ', '.join(database_names))
print("Collections: " + ', '.join(collection_names))

# mongoimport --db tourPedia --collection paris --username root --password root --authenticationDatabase admin --type json --file /app/tourPedia_paris.json --jsonArray

# mongoimport --db tourPedia --collection adresse_paris --username root --password root --authenticationDatabase admin --type json --file /app/adresse_paris.json --jsonArray