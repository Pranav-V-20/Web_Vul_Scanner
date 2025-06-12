import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

xss_payloads = ["<script>alert(1)</script>"]
sqli_payloads = ["' OR '1'='1", "';--"]

def is_vulnerable(response, payload):
    return payload in response.text

def scan_xss(url):
    results = []
    forms = get_forms(url)
    for form in forms:
        action = form.get("action")
        post_url = urljoin(url, action)
        method = form.get("method", "get").lower()
        inputs = form.find_all("input")
        for payload in xss_payloads:
            data = {}
            for inp in inputs:
                name = inp.get("name")
                if name:
                    data[name] = payload
            if method == "post":
                res = requests.post(post_url, data=data)
            else:
                res = requests.get(post_url, params=data)
            if is_vulnerable(res, payload):
                results.append(("XSS", post_url, payload))
    return results

def scan_sqli(url):
    results = []
    for payload in sqli_payloads:
        new_url = f"{url}?id={payload}"
        res = requests.get(new_url)
        if re.search("sql|syntax|mysql|error", res.text, re.IGNORECASE):
            results.append(("SQLi", new_url, payload))
    return results

from .crawler import get_forms
