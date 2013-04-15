#!/usr/bin/env python

import requests

proxies = {
  "http": "127.0.0.1:8087",
  # "http": "http://user:pass@10.10.1.10:3128/"
}

g=requests.get("http://ifconfig.me/ip", proxies=proxies)
print g.content

