# -- coding: utf-8 --


es = Elasticsearch([{'host': "172.29.42.98", 'port': 9200}, {'host': "172.29.45.22", 'port': 9200},{'host': "172.29.45.81", 'port': 9201}], timeout=3600)

class  Essearch:
    def Escardno(self):
        body = {
        "query": {
            "match_all": {}
        },
        "from": "0",