#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

API_URL = 'http://unsplash.com/api/read'

def _get_xml_data(url):
    print url
    data = requests.get(url)
    if not data.ok or not data.content:
        return None
    result = BeautifulSoup(data.content)
    return result

def read_api(number_of_results = None):
    xml_data = _get_xml_data(API_URL)
    if not xml_data:
        return None
    total = number_of_results
    if not total:
        total = int(xml_data.findAll('posts')[0].get('total'))
    index = len(xml_data.findAll('post'))
    while index < total:
        url = API_URL + '?start=%d' % index
        xml_data = _get_xml_data(url)
        index += len(xml_data.findAll('post'))

class UnsplashData(object):
    '''
    Contains data from unsplash api.
    '''

    def __init__(self):
        self._images = []
        self._photographers = {}

    def get_images(self):
        return self._images

    def get_photographers(self):
        return self._photographers.values()

    def get_photographers_names(self):
        return self._photographers.keys()

    def get_photographer(photographer_name):
        return self._photographers.get(photographer_name, None)

# class 

# class WikipediaPage(object):
#   '''
#   Contains data from a Wikipedia page.
#   Uses property methods to filter data from the raw HTML.
#   '''

#   def __init__(self, title, redirect=True, preload=False, original_title=''):
#     self.title = title
#     self.original_title = original_title or title

#     self.load(redirect=redirect, preload=preload)

