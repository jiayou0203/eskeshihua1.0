from flask import Flask
from flask import render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
    es = Elasticsearch([{'host': "172.29.42.98", 'port': 9200}, {'host': "172.29.45.22", 'port': 9200},{'host': "172.29.45.81", 'port': 9201}], timeout=3600)
    body = {
        "query": {
            "match_all": {}
        },
        "from": "0",
        "size": "50"
    }
    search_result = es.search(index="preprod-2022.03.15", doc_type=None, body=body)
    search_result=search_result['hits']['total']['value']  #符合条件数据条目总数
    return render_template('index.html',u=search_result)



if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
