import codecs
import pickle
import json

# read data from file
handle = codecs.open('bigmir_pair_all.json','r', 'utf-8')
data = handle.read()
handle.close()
data = json.loads(data)
index_dict = {}
for d in data:
    key = d['url']
    index_dict[key] = d['id']

with open('bigmir_data.pickle', 'wb') as f:
    pickle.dump(index_dict, f)