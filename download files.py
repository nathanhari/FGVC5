# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:49:42 2018

@author: hari
"""

import json
import os
import requests

base_dir = 'D:\\Kaggle\\FGVC5'
json_fns = [fn for fn in os.listdir(base_dir) if fn.endswith('.json')]

for fn in json_fns:
    dataset = fn.split('.')[0]
    target_dir = os.path.join(base_dir, dataset)
    if os.path.exists(target_dir) == False:
        os.mkdir(target_dir)
    with open(os.path.join(base_dir, fn), 'r') as fp:
        json = json.load(fp)
    n_images = len(json['images'])
    i = 0
    for img in json['images']:
        imgid, url = img['imageId'], img['url']
        img_data = requests.get(url).content
        img_dir = os.path.join(target_dir, '{}.jpg'.format(imgid))
        if os.path.exists(img_dir) == False:
            with open(img_dir, 'wb') as handler:
                handler.write(img_data)
        i += 1
        if (i % 100) == 0:
            print('{}: {}/{} --> {}'.format(fn, i, n_images, i/n_images))