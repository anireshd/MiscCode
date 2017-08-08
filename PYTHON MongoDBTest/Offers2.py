import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client.OffersDB

f = open('H:\Fandango\Offers2.csv', 'w')

varBundle = []

for bundles1 in db.bundles.aggregate([{"$group": {"_id": "$Offer_id", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}]):
    varBundle.append(bundles1)

for offers1 in db.offers.find({}, {"Offer_id": 1, "Offer_nm": 1, "_id": 0}):

   for x in varBundle:

       if offers1["Offer_id"] == x["_id"]:
            print('"%s","%s","%s", %d' % (offers1["Offer_nm"], offers1["Offer_id"], x["_id"], x["count"]))
            f.write('"%s","%s",%d' % (offers1["Offer_nm"], x["_id"], x["count"]))
            f.write("\n")

f.write("Total Bundles= %d" % db.bundles.count())
f.write("\n")
f.write("Total Offers= %d" % db.offers.count())
f.close()

