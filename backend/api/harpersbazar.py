'''
API which scrap the harpersbazar website and return the data in the form of a list of lists.

'''

from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories

harpersbazar = Blueprint('harpersbazar', __name__, url_prefix='/harpersbazar')


def fetch_harpersbazar():
    source = requests.get(
        'https://www.harpersbazaar.com/fashion/trends/')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find_all('a')
    #print(div)
    data = []
    post = []

    for link in div:
        local_link = link.get('href')
        a = str(link.get('href')).split('/')

        if len(a) > 2 and a[1] == 'fashion' and a[2] == 'trends':
            data.append('https://www.harpersbazaar.com' + local_link)

    data = list(set(data))

    '''
        Scraping all the links from the post links and storing them in a list.
    '''

    for idx in range(0, len(data)):
        link = data[idx]
        #print(link)
        link_source = requests.get(link)
        link_htmlContent = link_source.content
        link_soup = BeautifulSoup(link_htmlContent, 'html.parser')
        link_div = link_soup.find_all('div')
        para = []
        for link_para in link_div:

            if link_para.has_attr('class') and link_para.get('class')[0] == 'listicle-intro':
                if link_para.text:
                    link_para = link_para.text
                    link_para.replace('\n', '')
                    link_para = re.split(' |\n |, |\r |\t |  ', link_para)
                    if(link_para):
                        para.extend(list(set(link_para)))
        if para:
            post.append([link, para])

    return post


@harpersbazar.route('/', methods=['GET'])
def get_harpersbazar():
    harpersbazar_ = fetch_harpersbazar()
    return json.dumps(harpersbazar_)
