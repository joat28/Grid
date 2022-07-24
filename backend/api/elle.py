'''
API which scrap the elle website and return the data in the form of a list of lists.

'''

from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories

elle = Blueprint('elle', __name__, url_prefix='/elle')


def fetch_elle():
    source = requests.get(
        'https://www.elle.com/fashion/trend-reports/')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find_all('a')
    #print(div)
    data = []
    post = []

    for link in div:
        local_link = link.get('href')
        a = str(link.get('href')).split('/')
        # print(a)

        if len(a) > 2 and a[1] == 'fashion' and a[2] == 'trend-reports':
            data.append('https://www.elle.com' + local_link)

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
        for link_para in link_div:

            if link_para.has_attr('class') and link_para.get('class')[0] == 'body-text':
                # print(link_para.text)
                link_para = re.split(' |\n |, |\r |\t |  ', link_para.text)
                link_para = list(set(link_para))
                post.append([link, link_para])

    return post


@elle.route('/', methods=['GET'])
def get_elle():
    elle_ = fetch_elle()
    return json.dumps(elle_)
