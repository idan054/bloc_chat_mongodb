import os

import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API

from enum import Enum

class ReqType(Enum):
    POST = 'post'
    GET = 'get'



def woo_req_base(reqType, base_url, path, consumer_secret, consumer_key, params):

    try:
        # endpoint = f'{base_url}/wp-json/wc/v3/products/categories?per_page=100&_fields=id,name'
        endpoint = f'{base_url}{path}'

        if reqType == ReqType.GET:
           response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        elif reqType == ReqType.POST:
           response = requests.post(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret), params=params)

        if response.status_code == 200:
            categories = response.json()

            # file_path = os.path.join(os.getcwd(), 'categories.json')
            # Write the categories to a file
            # with open(file_path, mode='w') as file:
            #     json.dump(categories, file, ensure_ascii=False, indent=4)

            return response.json()

        return errList

    except:
        return errList


errList = [

    {
        'id': 0,
        'name': '1. מידע לא זוהה - נא לפנות אל האיש הטכני / מנהל האתר',
    },

    {
        'id': 1,
        'name': '2. קטגוריות לא זוהו - יש לוודא שהמפתח CS CK תקינים והמפתח משוייך למשתמש מנהל https://ibb.co/Y35cVRD',
    },

    {
        'id': 2,
        'name': '3. קטגוריות לא זוהו - יש לוודא שכתובת האתר הוזנה בצורה תקינה https://your-site.co.il',
    },

    {
        'id': 3,
        'name': '4. קטגוריות לא זוהו - ייתכן שהשרת / אתר שלך חוסם את הבקשה כאמצעי הגנה למניעת CORS',
    }
]