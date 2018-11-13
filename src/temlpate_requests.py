import os
import requests
import codecs
import configparser
import time
import datetime
from bs4 import BeautifulSoup as BS
from elasticsearch import Elasticsearch
from random import randint

domain = 'http://forum.dneprcity.net/'

headers = [
    {'User-Agent': 
        'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 
        'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]
TODAY = datetime.datetime.now()
today_topic_time = TODAY.strftime("%d/%m/%y") + ' '
two_hours_ago = int(TODAY.timestamp()) - 120*60
foundtime = 0
data = []    

# config = {}
# cparser = configparser.ConfigParser()
# cparser.read("socmonitor.conf")
# path_items = cparser.items( "config" )
# for key, value in path_items:
#     config[key] = value
#
def parse_(): 
    # try:
    #     es = Elasticsearch(config['es_url'], http_auth=(config['es_name'], 
    #                                                     config['es_password']))
    #     q = es.search(index='forums', body={"query": {"match": {"domain": domain}},
    #                                         "sort": [{ "foundtime": "desc" }]})
    # except:
    #     print('ElasticSearch is not available!')
    #     pass
    # else:
    #     total = q['hits']['total']
    #     if total > 0:
    #         hit = q['hits']['hits'][0]
    #         foundtime = hit['_source']['foundtime']
    #         if foundtime < two_hours_ago:
    #             foundtime = two_hours_ago
    #     else:
    #         foundtime = two_hours_ago

    if True:
        session = requests.Session()
        nmb = randint(0, 2)
        resp = session.get(domain, headers=headers[nmb])
        topics_url = []
        if resp.status_code == 200:
            soup = BS(resp.content, "html.parser")
    
    data = soup.prettify()
    handle = codecs.open('temp.html', "w", 'utf-8')
    handle.write(str(data))
    handle.close()    
    return True




if __name__ == '__main__':
    print(parse_())        


