import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API


def product_details_by_name(web_field, cs_field, ck_field, main_field):

    base_url = web_field
    consumer_key = ck_field
    consumer_secret = cs_field

    product_name = main_field

    endpoint = f'{base_url}/wp-json/wc/v3/products?_fields=id,name,price,sku,images,description,permalink'
    params = {
        'search': product_name,
        'per_page': 1
    }

    # wcapi = API(
    #     url=base_url,
    #     consumer_key=consumer_key,
    #     consumer_secret=consumer_secret,
    #     version="wc/v3"
    # )
    # productss = wcapi.get("products", params={"per_page": 20})
    # return str(productss)
    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MDMzMzEyNzcsImV4cCI6NzcwMzMzMTIxNywiZW1haWwiOiJvc3BpZGVyM2RAZ21haWwuY29tIiwiaWQiOiI0NzY0Iiwic2l0ZSI6Imh0dHBzOlwvXC93d3cuc3BpZGVyM2QuY28uaWwiLCJ1c2VybmFtZSI6ImV5YWwxMGJpdEBnbWFpbC5jb20ifQ.xVQAxHdyMINU_oK3wBniOmJb8qVb0c0xxAr2ncyNlog"
    # }

    # 'https://corsproxy.io/?https://spider3d.co.il/wp-json/wc/v3/products?search=כחול&consumer_key=ck_10860d370ddb79f39b4da3a765960cfd05842cfa&consumer_secret=cs_5265e43f6e72275fc510c86dee08ae81b08c8e97'

    response = requests.get(endpoint,
                            # headers=headers,
                            params=params,
                            auth=HTTPBasicAuth(consumer_key, consumer_secret),
                            )

    if response.status_code == 200:

        products = response.json()
        if products:
            # print(products[0])

            # Exanple: https://spider3d.co.il/wp-json/wc/v3/products?search=%D6%BC%D6%BC+PLA%D6%BC%20%D7%A1%D7%99%D7%9C%D7%A7%20%D7%9E%D7%98%D7%90%D7%9C%D7%99%20%D7%90%D7%93%D7%95%D7%9D%20Silk%20Red&consumer_key=ck_10860d370ddb79f39b4da3a765960cfd05842cfa&consumer_secret=cs_5265e43f6e72275fc510c86dee08ae81b08c8e97

            try:
                permalink = products[0]['permalink']
            except KeyError:
                permalink = '-'

            try:
                id = products[0]['id']
            except KeyError:
                id = '-'

            try:
                name = products[0]['name']
            except KeyError:
                name = '-'

            try:
                price = products[0]['price']
            except KeyError:
                price = '-'

            try:
                sku = products[0]['sku']
            except KeyError:
                sku = '-'

            try:
                image = products[0]['images'][0]['src']
            except (KeyError, IndexError):
                image = '-'

            try:
                description_html = products[0]['description']
                clean_desc = extract_text_from_html(description_html)
            except KeyError:
                description_html = '-'
                clean_desc = '-'

            product_values = [permalink, id, name, clean_desc, price, image, sku]
            addRows(product_values)
            return product_values
        else:
            print("Product not found.")
            return []
    else:
        print("Failed to retrieve products. Status code:", response.status_code)
        return []


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator='\n', strip=True)
