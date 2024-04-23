from flask import Flask, jsonify, request
import products_dao 
import uom_dao
from sql_connection import get_sql_connection

app = Flask(__name__)


connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    responce = jsonify(products)
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce


@app.route('/getUOM', methods=['GET'])
def get_UOMs():
    uom = uom_dao.get_uoms(connection)
    response = jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    responce = jsonify({
        'product_id': return_id
    })
    responce.headers.add('Access-Control-Allow-Origin', '*')
    return responce


if __name__ == "__main__":
    
    app.run(port=5000)