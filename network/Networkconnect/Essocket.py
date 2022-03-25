# -- coding: utf-8 --
# -- coding: utf-8 --



from elasticsearch import Elasticsearch
import Netsocket
import requests
import  ast

es = Elasticsearch([{'host': "172.29.42.98", 'port': 9200}, {'host': "172.29.45.22", 'port': 9200},{'host': "172.29.45.81", 'port': 9201}], timeout=3600)

class  Essearch:

    def Esindex(self,eshost):
        netconnt=Netsocket.Networkconnect()
        self.url="http://"+eshost+"/_cat/indices"
        index=requests.get(self.url)
        index.str=index.text
        index_zhi=index.str.split()
       # print(len(index_zhi))
        index=[]
        index.append(index_zhi[2])
        i=2
        while i<860:
              index.append(index_zhi[i])
              i+=10
              print(i)
        return index

    def Escardno(self):
        body = {
        "query": {
            "match_all": {}
        },
        "from": "0",
        "size": "50"
    }
        search_result = es.search(index="preprod-2022.03.15", doc_type=None, body=body)
        search_result = search_result['hits']['total']['value']  # 符合条件数据条目总数
        return  search_result
