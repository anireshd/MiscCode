import pymongo
import pprint

client = pymongo.MongoClient('localhost', 27017)

db = client.restaurants
#for restaurant in db.restaurants.find({'grades.score': {"$gt": 50}}):
#    pprint.pprint('Restaurant %s is at zipcode %s grade: %s'
#                  % (restaurant["name"], restaurant["address"]["zipcode"],restaurant["grades"].pop()["grade"]))

#for rest1 in db.restaurants.aggregate([{"$group":{"_id":"$cuisine","count":{"$sum":1}}},{"$sort":{"_id":1}}]):
 #   pprint.pprint('%s - %d' % (rest1["_id"], rest1["count"]))

f = open('H:\Fandango\Restaurants.csv', 'w')

for rest2 in db.restaurants.aggregate([{"$group":{"_id":"$cuisine","count":{"$sum":1}}},{"$sort":{"count":-1}}]):
    pprint.pprint('%s - %d' % (rest2["_id"], rest2["count"]))
    f.write('"%s",%d' % (rest2["_id"], rest2["count"]))
    f.write("\n")

f.write("total = %d" % db.restaurants.count())
f.close()

