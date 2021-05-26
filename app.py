from flask import Flask
from flask_restx import Resource, Api
from upbit_m import *
from flask_cors import CORS
import multiprocessing
import time
from thread_process import *
from ramdom_name import ran_name
from random_lotto import *

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

api = Api(
    app,
    version='0.1',
    title="orclord's API Server",
    description="orclord bitcoin API Server!",
    terms_url="/",
    contact="orclord82@gmail.com",
    license="MIT"
)

thread_List = list()
@app.route("/myapi")
def get_KRW():  # 멤버 함수의 파라미터로 name 설정
    value = lotto_a(10000)    
    return {"message":value}  

@app.route("/myapi/1")
def get_KRW2():  # 멤버 함수의 파라미터로 name 설정

    value = format(int(get_balance("KRW")), ",")
    
    return {"message":"현재 잔고 : {} 원".format(value),"data":[]}    
    # return {"message":"6666666"}  

@app.route("/myapi/2")
def get_KRW3():  # 멤버 함수의 파라미터로 name 설정
    value = format(int(get_current_price("KRW-ETH")),",")
    return {"message":"ETH 현재 가격 : {}".format(value),"data":[]}  

@app.route("/myapi/3")
def get_KRW4():  # 멤버 함수의 파라미터로 name 설정
 
    data = get_balance('all')
    return {"message":"------총 잔고현황------","data":data}

@app.route("/hello")
def get_hello():  # 멤버 함수의 파라미터로 name 설정
    
    
    return {"message": "쓰레드 리스트 : {}".format(thread_List),"data":[]}
 
@app.route("/hello/<string:name>")  # url pattern으로 name 설정
def get(name):  # 멤버 함수의 파라미터로 name 설정
    try:

        if name == "True":
            thread_List.append(ran_name)
            thread_List[-1] = multiprocessing.Process(target=b)
            thread_List[-1].start()
            memo = "스타트 프로세서"
        elif name =="False":
            if thread_List != []:
                thread_List[-1].terminate()
                del thread_List[-1]
                memo = "종료 프로세서"
            else:
                memo = "모든 프로세서가 종료된 상태"
                pass
        else:
            memo = "잘못된 접근입니다."
    except Exception as e:
        print(e)
        memo=e
        pass
    finally:
        print(thread_List)
        # for process in thread_List:
        #     process.terminate()
    return {"message" : "Welcome, {}{}!".format(memo,thread_List),"data":[]}

# @app.route('/hello')  # url pattern으로 name 설정
# class Hello(Resource):
#     def get(self):  # 멤버 함수의 파라미터로 name 설정
#         return {"message":str(get_balance("KRW"))}  
#sdf


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    