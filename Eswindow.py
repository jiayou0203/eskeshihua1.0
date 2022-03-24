from flask import Flask
from flask import render_template
from  network.Networkconnect import Essocket


app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

'''
@app.route('/module')
def module():
    return render_template('index.html',u=search_result)
'''

@app.route('/index')
def index():
    eslist={'172.29.42.98:9200','172.29.45.22:9200','172.29.45.81:9200'}
    for  eshost  in  eslist:
         search_index=Essocket.Essearch().Esindex(eshost)
    return render_template('index.html',u=search_index)




if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
