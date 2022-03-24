# -- coding: utf-8 --
from elasticsearch import Elasticsearch
from netwrok.Networkconnect import Netsocket


es = Elasticsearch([{'host': "172.29.42.98", 'port': 9200}, {'host': "172.29.45.22", 'port': 9200},{'host': "172.29.45.81", 'port': 9201}], timeout=3600)

class  Essearch:
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