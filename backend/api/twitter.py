from flask import jsonify, Blueprint, request
from requests_html import HTMLSession
import asyncio
from api.helper.categories import get_categories

twitter = Blueprint('twitter', __name__,url_prefix='/twitter')

def fetch_all():

    all_data = []
    
    total_categories = get_categories()

    for categories in get_categories():
        
        for subcategory in total_categories[categories]:
            # print(subcategory)
            url = f'https://twitter.com/search?q={subcategory}&src=typed_query&f=image'
            session = HTMLSession()
            response = session.get(url)
            subcategory_list = []
            
            tweets = response.html.find('img')
            print(tweets)

            
            #css-1dbjc4n
            # for items in tweets:
                #print(items)
                # try:
                #     tweet_img = items.find('img.css-9pa8cd')[0].attrs['src']
                #     subcategory_list.append(str(tweet_img))
                #     print(tweet_img)
                # except:
                #     pass
            all_data.append({subcategory:subcategory_list})
        print("\n")
    return all_data

@twitter.route('/', methods=['POST'])
def get_twitter_data():
    try:
        req = request.get_json()
        category_fetched = str(req['category_item'])

    except Exception as e:
        return jsonify({"error": str(e)})
    
    if category_fetched == 'all':
        final_twitter_data = fetch_all()
        return final_twitter_data
    elif category_fetched == 'mens':
        final_twitter_data = fetch_all()
        return jsonify(final_twitter_data)
    elif category_fetched == 'womens':
        final_twitter_data = fetch_all()
        return jsonify(final_twitter_data)
    elif category_fetched == 'kids':
        final_twitter_data = fetch_all()
        return jsonify(final_twitter_data)