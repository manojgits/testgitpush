import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.f5e76.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"Manoj",
    "email":"Manoj@gamail.com",
    "Surname":"Kumar"
}
db1=client['Mongotest']
coll=db1['test']
coll.insert_one(d)
