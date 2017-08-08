import pymongo
import pprint

client = pymongo.MongoClient('localhost', 27017)

db = client.OffersDB

f = open('H:\Fandango\Offers.csv', 'w')

#pipe = [{'$group': {'_id': None, 'total': {'$sum': '$bundles'}}}]

#db.bundles.aggregate(pipeline=pipe)

for rest2 in db.bundles.aggregate([{"$group":{"_id":"$Offer_id","count":{"$sum":1}}},{"$sort":{"count":-1}}]):
    pprint.pprint('%s - %d' % (rest2["_id"], rest2["count"]))
    f.write('"%s",%d' % (rest2["_id"], rest2["count"]))
    f.write("\n")

f.write("total = %d" % db.bundles.count())
f.close()

