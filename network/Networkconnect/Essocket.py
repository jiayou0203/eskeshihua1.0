# -- coding: utf-8 --
from elasticsearch import Elasticsearch
from network.Networkconnect import Netsocket


es = Elasticsearch([{'host': "172.29.42.98", 'port': 9200}, {'host': "172.29.45.22", 'port': 9200},{'host': "172.29.45.81", 'port': 9201}], timeout=3600)

class  Essearch:

    def Esindex(self,eshost):
        netconnt=Netsocket.Networkconnect
        self.url=eshost+"/_cat/indices"
        index=netconnt.netconn().get(self.url)
        return index

    def Escardno(self):
        body = {
        "query": {
            "match_all": {}
        },
        "from": "0",
        "size": "50"
    }
        search_result = es.search(index="actuator", doc_type=None, body=body)
        search_result = search_result['hits']['total']['value']  # 符合条件数据条目总数
        return  search_result