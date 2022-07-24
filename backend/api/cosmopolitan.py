'''
API which scrap the cosmopolitan website and return the data in the form of a list of lists.

'''

from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories

cosmopolitan = Blueprint('cosmopolitan', __name__, url_prefix='/cosmopolitan')


def fetch_cosmopolitan():
    source = requests.get(
        'https://www.cosmopolitan.com/style-beauty/fashion/')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find_all('a')
    
    data = []
    post = []
    
    for link in div:
        if link.get('data-vars-ga-outbound-link'):
            data.append(link.get('data-vars-ga-outbound-link'))


    data = list(set(data))

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
            if link_para.has_attr('class') and link_para['class'][0] == 'body-dropcap':
                link_para = link_para.text
                if (link_para):
                    link_para.replace('\n', '')
                    link_para = re.split(' |\n |, |\r |\t |  ', link_para)
                    if link_para:
                        para.extend(list(set(link_para)))
        if para:
            post.append([link, para])
    return post


@cosmopolitan.route('/', methods=['GET'])
def get_cosmopolitan():
    cosmopolitan_ = fetch_cosmopolitan()
    return json.dumps(cosmopolitan_)
