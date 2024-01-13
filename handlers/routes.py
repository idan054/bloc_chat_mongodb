import os
import pandas as pd
from flask import render_template, request, json
from modules.woo_requests.product_details_by_name import product_details_by_name
from modules.woo_requests.products_from_category import get_products_from_category
from modules.woo_requests.woo_req_base import ReqType, woo_req_base


def configure_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route('/success', methods=['POST', 'GET'])
    def success():

        if request.method == 'POST':
            data = request.get_json()
            main_field = data['main_field']
            selectedRadioValue = data['selectedRadioValue']
            web_field = data['web_field']
            ck_field = data['ck_field']
            cs_field = data['cs_field']

            # 0 = One product, not category
            if selectedRadioValue == 0:
                product_details_by_name(web_field, cs_field, ck_field, main_field)
            else:
                get_products_from_category(web_field, cs_field, ck_field, main_field, selectedRadioValue)

        return render_template('success.html')

    @app.route('/get_category', methods=['POST', 'GET'], )
    def get_category():
        if request.method == 'POST':
            print("START /get_category")
            print(request.get_json())
            data = request.get_json()
    
            resp = woo_req_base(
                    path='/wp-json/wc/v3/products/categories?per_page=100&_fields=id,name',
                    reqType=ReqType.GET,
                    params={},

                    base_url=data['web_field'],
                    consumer_secret=data['cs_field'],
                    consumer_key=data['ck_field'],
                )
            
            return resp
