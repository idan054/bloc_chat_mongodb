import os

import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API

from modules.woo_requests.woo_req_base import ReqType, woo_req_base

