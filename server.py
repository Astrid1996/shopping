from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('week2_DamiPark.html')


## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    delivery_address_receive = request.form['delivery_address_give']
    call_receive = request.form['call_give']

    order = {
       'name': name_receive,
       'quantity': quantity_receive,
       'address': delivery_address_receive,
       'call' : call_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '구매가 성공적으로 완료되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)