#!/usr/bin/python
# -- coding: utf-8 --

from elasticsearch import Elasticsearch

ES=[
    "172.29.42.98:9200",
    "172.29.45.22:9200",
    "172.29.45.81:9200"
]
# elasticsearch集群服务器的地址
es = Elasticsearch(ES,
                   sniff_on_start=True,
                   #启动前嗅探es集群服务器
                   sniff_on_connection_fail=True,
                   # es集群服务器结点连接异常时是否刷新es节点信息
                   sniff_timeout=60
                   # 每60秒刷新节点信息
                   )


if __name__=='__main__':
    body = {
        "query": {
            "term": {
                "message": "cardno"
            }
        },
        "from": "0",
        "size": "50"
    }
    '''
    body={
      "query":{
                "match_all": {}
               },
        "from": "0",
        "size": "50"
    }
    #查询所有结果
    #
    '''


    #查询message字段中包含cardno关键字
    search_result=es.search(index="preprod-2022.03.15",doc_type=None,body=body)
    print(search_result['hits']['hits'][1]['_source']['message'])
    print(len(search_result['hits']['hits']))
    for  i in range(len(search_result['hits']['hits'])):
           print(search_result['hits']['hits'][i]['_source']['message'])