'''
API which scrap the vogue website and return the data in the form of a list of lists.

'''

from urllib.request import urlopen
from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories

vogue = Blueprint('vogue', __name__, url_prefix='/vogue')


def fetch_vogue():
    source = requests.get(
        'https://www.vogue.in/fashion/fashion-trends')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find_all('a')
    # print(div)
    data = []
    post = []

    for link in div:
        local_link = link.get('href')
        a = str(link.get('href')).split('/')
        # print(a)

        if len(a) > 3 and a[1] == 'fashion' and a[2] == 'content':
            data.append('https://www.vogue.in' + local_link)

    data = list(set(data))
    # print(len(data))
    '''
        Scraping all the links from the post links and storing them in a list.
    '''

    for idx in range(0, len(data)):
        link = data[idx]
        # print(link)
        link_source = requests.get(link)
        link_htmlContent = link_source.content
        link_soup = BeautifulSoup(link_htmlContent, 'html.parser')
        link_div = link_soup.find_all('p')
        para = []
        for link_para in link_div:

            link_para = link_para.text
            if (link_para):
                link_para.replace('\n', '')
                link_para = re.split(' |\n |, |\r |\t |  ', link_para)
                if link_para:
                    para.extend(list(set(link_para)))
        if para:
            post.append([link, para])
    # print(len(post))
    return post


@vogue.route('/', methods=['GET'])
def get_vogue():
    vogue_ = fetch_vogue()
    return json.dumps(vogue_)
