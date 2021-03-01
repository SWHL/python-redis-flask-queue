# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: test2.py
# @Time: 2021/02/28 20:32:36
# @Author: Max
import time

import requests

post_url = "http://0.0.0.0:5000"
post_result = requests.post(post_url, data={'x': 2})
job_id = post_result.text
print(job_id)

time.sleep(3)

get_url = "http://0.0.0.0:5000/result/{}".format(job_id)
get_result = requests.get(get_url)
print(get_result.content)
