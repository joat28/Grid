from flask import jsonify, Blueprint, request
import requests
import json
from api.helper.categories import get_categories 

twitter = Blueprint('twitter', __name__,url_prefix='/twitter')

def get_tweets(searchKeyword):
    url = f'https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q={searchKeyword}&result_filter=image&count=20&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control'
    payload={}
    headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'personalization_id="v1_bEUDUwTKcsKbauQzJntf4g=="; guest_id=v1%3A163509007848027860; guest_id_marketing=v1%3A163509007848027860; guest_id_ads=v1%3A163509007848027860; g_state={"i_p":1648317095114,"i_l":4}; ads_prefs="HBERAAA="; kdt=6Yd8W6XRml4HCgGOKVcZg4xhhK7K5ams0MeLlkz6; auth_token=916bc87b608651eca2a1079699d12a1a2ef3f82c; twid=u%3D1356707339554889729; ct0=2c704ce10ed8895c558a29725a07a2e9eb0feabe9ef42c60947ac5867b106fe6f5d8e5f9c5ea3e220682f99cca48ac487b6737f7afddb5c561df41fa9c7c5c3e97160453237367e05325465193ef9964; mtc_opt_in=Y; _ga_WQTQ9YMFLG=GS1.1.1657783423.1.1.1657783538.0; des_opt_in=Y; _gcl_au=1.1.528138554.1657784095; mbox=PC#981a8642ed6a46fdb75477c8a5ad428e.31_0#1721115097|session#f4d4265610eb4300ac0f9f60a35e143a#1657872157; _ga_34PHSZMC42=GS1.1.1657870322.2.0.1657870568.0; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _ga=GA1.2.2097042372.1635090089; _gid=GA1.2.242019431.1658049716; lang=en; ct0=3deb8176593da06aff4c1e36dc0cf3bd88a3ce818a3841ed7b568f8b14e77a16818271836ebe94a91da5b00b6acba20001699bd6017ef6c507eb2e3b8ac503fed19540e95c534b31e12eef10196587dc; guest_id=v1%3A165813359025819934; guest_id_ads=v1%3A165813359025819934; guest_id_marketing=v1%3A165813359025819934; personalization_id="v1_1ERNbqIOzyF5mqF8h5+hiA=="',
    'referer': f'https://twitter.com/search?q={searchKeyword}&src=typed_query&f=image',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': '2c704ce10ed8895c558a29725a07a2e9eb0feabe9ef42c60947ac5867b106fe6f5d8e5f9c5ea3e220682f99cca48ac487b6737f7afddb5c561df41fa9c7c5c3e97160453237367e05325465193ef9964',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    tweets = response.json()['globalObjects']['tweets']
    return tweets

def fetch_by_keyword(searchKeyword):
    tweets = get_tweets(searchKeyword)
    data = []
    for key in tweets:
        data.append({
            'tweet_url': tweets[key]['entities']['media'][0]['expanded_url'],
            'image_url': tweets[key]['entities']['media'][0]['media_url'],
            'likes': tweets[key]['favorite_count'],
            'retweets': tweets[key]['retweet_count'],
            'replies': tweets[key]['reply_count'],
            'description': tweets[key]['full_text']
        }) 
    return json.dumps(data)

def fetch_all():
    categories = get_categories()
    return categories

#--------------Routes--------------------

#Get tweets corresponding to all possible categories in fashion
@twitter.route('/tweet/', methods=['GET'])
def get_all_tweets():
    return fetch_all()

#Get tweets correspoding to a specific item in fashion
@twitter.route('/tweet/query=<searchKeyword>', methods=['GET'])
def get_tweets_keyword(searchKeyword):
    return fetch_by_keyword(searchKeyword)

