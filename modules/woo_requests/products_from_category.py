import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API
import pandas as pd
from modules.addRow import addRows
from modules.woo_requests.product_details_by_name import extract_text_from_html


def get_products_from_category(web_field, cs_field, ck_field, mainFieldNum, categoryId):
    base_url = web_field
    consumer_key = ck_field
    consumer_secret = cs_field

    # base_url = 'https://spider3d.co.il'
    # consumer_key = 'ck_10860d370ddb79f39b4da3a765960cfd05842cfa'
    # consumer_secret = 'cs_5265e43f6e72275fc510c86dee08ae81b08c8e97'
    # product_name = 'חומר גלם'

    # file_path = 'settings.txt'
    # config = {}
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         key, value = line.strip().split('=')
    #         config[key.strip()] = value.strip()
    #
    # base_url = config.get('base_url', '')
    # consumer_key = config.get('consumer_key', '')
    # consumer_secret = config.get('consumer_secret', '')

    endpoint = f'{base_url}/wp-json/wc/v3/products?_fields=id,name,price,sku,images,description,permalink'
    params = {
        'category': categoryId,
        'per_page': 30,
        'page': mainFieldNum
    }

    response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret), params=params)

    product_list_values = []
    if response.status_code == 200:
        products = response.json()
        if products:
            for product in products:
                # print(product)
                # Exanple: https://spider3d.co.il/wp-json/wc/v3/products?search=%D6%BC%D6%BC+PLA%D6%BC%20%D7%A1%D7%99%D7%9C%D7%A7%20%D7%9E%D7%98%D7%90%D7%9C%D7%99%20%D7%90%D7%93%D7%95%D7%9D%20Silk%20Red&consumer_key=ck_10860d370ddb79f39b4da3a765960cfd05842cfa&consumer_secret=cs_5265e43f6e72275fc510c86dee08ae81b08c8e97

                try:
                    permalink = product['permalink']
                except KeyError:
                    permalink = '-'

                try:
                    id = product['id']
                except KeyError:
                    id = '-'

                try:
                    name = product['name']
                except KeyError:
                    name = '-'

                try:
                    price = product['price']
                except KeyError:
                    price = '-'

                try:
                    sku = product['sku']
                except KeyError:
                    sku = '-'

                try:
                    image = product['images'][0]['src']
                except (KeyError, IndexError):
                    image = '-'

                try:
                    description_html = product['description']
                    clean_desc = extract_text_from_html(description_html)
                except KeyError:
                    description_html = '-'
                    clean_desc = '-'

                product_values = [permalink, id, name, clean_desc, price, image, sku]

                product_list_values.append(product_values)

            print("product_list_values")
            print(product_list_values)
            addRows(product_list_values)

            # df = pd.DataFrame(product_list_values)
            # df.columns = ["permalink", "id", "name", "clean_desc", "price", "image", "sku"]
            # file_name = "category_" + categoryId + ".xlsx"
            # df.to_excel(file_name, index=False, engine='openpyxl')

        return products
    return None
