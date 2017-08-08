import elasticsearch
es = elasticsearch.Elasticsearch()  # use default of localhost, port 9200
es.index(index='posts', doc_type='blog', id=2, body={
    'author': 'Benjamin Pollack',
    'blog': 'bitquabit',
    'title': 'Having Fun: Python and Elasticsearch',
    'topics': ['elasticsearch', 'python', 'parseltongue'],
    'awesomeness': 0.7
})
es.index(index='posts', doc_type='blog', id=3, body={
    'author': 'Benjamin Pollack',
    'blog': 'bitquabit',
    'title': 'How to Write Clickbait Titles About Git Being Awful Compared to Mercurial',
    'topics': ['mercurial', 'git', 'flamewars', 'hidden messages'],
    'awesomeness': 0.95
})
print(es.search(index='posts', q='author:"Benjamin Pollack"'))