from distutils.log import debug
from flask import Flask #載入Flask
import datetime
app =Flask(__name__)    #建立application 物件

#建立網站首頁回應方式
@app.route("/")
def index():    #用來回應網站首頁連線的含式
    return "Hello ,this is doiya"    #回傳網站首頁內容

@app.route("/datetime")
def date():    
    return str(datetime.datetime.now())
#啟動網站伺服器

if __name__=="__main__":
    app.run()(host='127.0.0.1',port=5000,debug=True)