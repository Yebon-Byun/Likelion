from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.likelion

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'매트릭스'})
print (target_movie['star'])