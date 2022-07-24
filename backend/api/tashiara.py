'''
API which scrap the tashiara (fashion influencer) website and return the data in the form of a list of lists.

'''


from operator import le
from urllib.request import urlopen
from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories

tashiara = Blueprint('tashiara', __name__, url_prefix='/tashiara')


def fetch_tashiara():
    source = requests.get(
        'https://www.tashiara.com/search/label/Style')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'lxml')
    div = soup.find_all('a')
    # print(div)
    data = []
    post = []

    for link in div:
        local_link = link.get('href')
        a = str(link.get('href')).split('/')
        # print(a)

        if len(a) > 3 and a[2] == 'www.tashiara.com' and a[3] >= '2022' and a[3].isalnum():
            data.append(local_link)

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
        link_soup = BeautifulSoup(link_htmlContent, 'lxml')
        link_div = link_soup.find_all('div')
        para = []
        for link_para in link_div:

            if link_para.text:
                link_para = link_para.text
                # print(link_para)
                link_para.replace('\n', '')
                link_para = re.split(
                    ' |\n |, |\r |\t |  |\n\n|\n\n\n\n', link_para)
                if(link_para):
                    para.extend(list(set(link_para)))

        if para:
            para = list(set(para))
            post.append([link, para])

    # print(len(post))
    return post


@tashiara.route('/', methods=['GET'])
def get_tashiara():
    tashiara_ = fetch_tashiara()
    return json.dumps(tashiara_)
