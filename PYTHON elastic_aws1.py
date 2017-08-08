import urllib3
import json
import elasticsearch
'''
put_body = json.dumps({
	"id":2,
    "title": "Airlift",
    "director": "Raja Krishna Menon",
    "year": 2016
})


http = urllib3.PoolManager()

r = http.request('POST', 'search-fandango-alpha-ijuayomdx6crobaz3zduipox3a.us-west-2.es.amazonaws.com/movie/year',
                 headers={'Content-Type': 'application/json'},
                 body=put_body)
				 
get_body = json.dumps({
"query":{
"match_all":{}
}
})	
				 
r1 = http.request('POST', 'search-fandango-alpha-ijuayomdx6crobaz3zduipox3a.us-west-2.es.amazonaws.com/movie/year/_search',
                 headers={'Content-Type': 'application/json'},
                 body=get_body)				 

'''
es = elasticsearch.Elasticsearch('https://search-fandango-alpha-ijuayomdx6crobaz3zduipox3a.us-west-2.es.amazonaws.com')

print(es.search(index='movie', q='id:1'))

