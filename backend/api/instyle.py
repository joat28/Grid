'''
API which scrap the instyle.com website and return the data in the form of a list of lists.

'''
from cgitb import html
from flask import jsonify, Blueprint, request
from bs4 import BeautifulSoup
import requests
import json
import re
from api.helper.categories import get_categories 

instyle = Blueprint('instyle', __name__, url_prefix='/instyle')



def fetch_instyle():
    source = requests.get('https://www.instyle.com/fashion/seasonal')
    htmlContent = source.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    div = soup.find_all('div')
    
    
    data = []
    post = []
    for para in div:
        '''
        Scraping all the 'a' tags from the html code.
        '''
        post_link = para.find_all('a')
        for link in post_link:
            
            if link.has_attr('class') and link['class'][0] == 'comp' and link['class'][-2] == 'card' and link['class'][-1] == 'card--no-image':
                post_link = link.get('href')
                data.append(post_link)
        # data contains all the post links trending on instyle.com related to the fashion.       
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
        link_div = link_soup.find_all('div')
        para = []
        for link_para in link_div:
            if link_para.has_attr('class') and link_para['class'][0] == 'comp' and link_para['class'][1] == 'article-content':
                if link_para.text:
                    link_para = link_para.text
                    # link_para.replace('\n', '')
                    link_para = re.split(' |\n |, |\r |\t |  ', link_para)
                    if(link_para):
                        para.extend(list(set(link_para)))
        if para:
            post.append([link, para])
    
    return post


    

@instyle.route('/', methods=['GET'])
def get_instyle():
    instyle_ = fetch_instyle()
    return json.dumps(instyle_)