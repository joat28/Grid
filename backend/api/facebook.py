from flask import Blueprint
import json
import requests

facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

#?sorting_setting=CHRONOLOGICAL&source=lhc&ref=nf

def fb_data(searchKeyword):
    url = 'https://www.facebook.com/api/graphql/'
    payload = 'av=100007288237916&__user=100007288237916&__a=1&__dyn=7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wIwh8KbgS3q2ibwyzE5S3O2Saxa1NwJwpUe8hwaG1sw9u0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782ly87e2l2Utwwwi82yxW1axe3e9wlo5qfK6E7e58jwGzEjxq1jxS6FobrwKxm5oe8cEW4-5pUfEdfwxwhFVovUy2a1yw9qm2Sq2-azqwaW22396w8m3216AzUjwTwNxe6U&__csr=gaY5k8NAcgKAxfbkaYAlk8nbiN_rsZnN7cxsSIXX9W9jqRkHGB8RbPFbiX9EJiLRRArSl5IKjpL8jqO9CR9iZlQ-HAXCilk-i88p6LGAypqWRWRXGqZ6DBmGRGjBAy49DCiWhECKlkExqWzFrQvVAAUGq8AKcGqbDAB8UkV8KbGuiEBGaKluunykdhA4U85hWnAKdxiu8AxuqE8kbKExrx7CxajwEzECmUvGezQqcUFyWVELzApxG3O5k49e5bybgyJ0wwgUswzK4EC8AxSbzoK5ohyUK68cUV1e68aXwMxm2he4Fo88S14whEaEc8ixq2e3Cbgux-3K4E9U7m0ka5UcUiw8K04Ao0orBU082U0j2G0IA3N280hrw8e0naUO16w0AAw1me08nw16Ze04NU8odu0PUcU3Cw8Fw4Wxa0z83uwWwZg7i0MVo1fUWbwm81LE15oG0I80k_w2QawAw7sw9S1Ez8igjw40w2Bo2hzoW880WC5o5W0a_wRG0cZw4EwSw5pw1xC0A81NE19E0NW0W8CE6GE1EUeopw&__req=bn&__hs=19192.HYP%3Acomet_pkg.2.1.0.2.0&dpr=1.5&__ccg=GOOD&__rev=1005868904&__s=p87gty%3A9f5ugo%3Ax12nca&__hsi=7121987746069150899&__comet_req=15&fb_dtsg=NAcPmENO1vhS-O919VSI4PMurJcC9mTgQcaJJ9c9u95NT0Vut-cNW9g%3A35%3A1658216990&jazoest=25183&lsd=1-ESj1NwWFjYAzT89bQKNy&__spin_r=1005868904&__spin_b=trunk&__spin_t=1658216991&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometInterestsDeepDivePostsListQuery&variables=%7B%22UFI2CommentsProvider_commentsKey%22%3A%22SearchCometInterestsDeepDiveRootQuery%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Atrue%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22feedLocation%22%3A%22SEARCH%22%2C%22feedbackSource%22%3A40%2C%22focusCommentID%22%3Anull%2C%22input%22%3A%7B%22extra_data%22%3A%22%7B%5C%22entry_point%5C%22%3A4%7D%22%2C%22scope_information%22%3Anull%2C%22session_id%22%3A%22487a709a-efee-409a-9ed5-fc25e89d75a4%22%2C%22topic_id%22%3A%22%23{searchKeyword}%22%2C%22explore_tab%22%3A%22TOP%22%7D%2C%22locale%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22search_results_page%22%2C%22scale%22%3A1.5%2C%22topic_results_paginating_after_cursor%22%3A%22%7B%5C%22current_section%5C%22%3A12%2C%5C%22serialized_section_cursor%5C%22%3A%5C%22%7B%5C%5C%5C%22serialized_browse_cursor%5C%5C%5C%22%3A%5C%5C%5C%22AbqKwf1-FgdfyhfPRxJ5Zpg-tr37iWVFmX5WlcMEAoPGDbF11BpN3xJ-EdiQzYW1h3j6jGPmtkvk45_0xF3hdbdg2gpxmP8TghIXXVC7lSbK20t43VJc1pQw3iEhACcS2mfXzs_2gm-pRpNKPkpipXKK0EmxImkbaHVueZ27KHeMbX2ombymnn3Kfa8MjJqzjkg7L4C4GFP1JQfQHRqsnGK0oSy_ooaaFI-96pJl-HcVfnVl0wr65YNXGRfMcJ37YwOe5s3W4Lgy2S4UbhivQ1dGfH_yhsGjjTtn9bgNGqbhmsG3SWNN3CBmdTXTrFYGCkT72f9OVfgHvdx1uDtVaX6Ds0KkBUeWLBw5nrixa9YegoJ2Rtb80n_69pgMcw1579c_Q8UkWJ48DgAcyRSUerix--jb0NA3m1T4u-w_8DsDtajsRvBYZ8ByjiQbkkzpOSuCdFl-eQ8V2VhQ_GjInVjBPTwnEsqfF5d0t2xMy-uNHcl6GLJ3kKOgw-nbHMvXX9Fo6GqR1P4c7Hjzs8IcBd_rY5hsNRG7aNW9enJ0LFL7ELj7XAu7PnBiOMBjtRZJaU-OTF2ZDxKFvVzka1vfZwklPc3Nc6YbdkE62NupTbXQvg%5C%5C%5C%22%2C%5C%5C%5C%22browse_unit_id%5C%5C%5C%22%3A%5C%5C%5C%22browse_serp%3A0cd2f481-1f8e-42b7-827f-a5a2fd26adf7%5C%5C%5C%22%2C%5C%5C%5C%22top_n_fbids_shown_at_start_of_section%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22session_id%5C%22%3A%5C%22487a709a-efee-409a-9ed5-fc25e89d75a4%5C%22%2C%5C%22current_page_num%5C%22%3A1%2C%5C%22section_to_num_results_shown%5C%22%3A%7B%5C%22top_posts%5C%22%3A2%7D%2C%5C%22top_n_fbids_shown%5C%22%3A%5B106091233641167%2C358339432324821%5D%2C%5C%22quick_promotion_fbids_shown%5C%22%3A%5B%5D%7D%22%2C%22topic_results_paginating_at_stream_enabled%22%3Afalse%2C%22topic_results_paginating_at_stream_initial_count%22%3A1%2C%22topic_results_paginating_first%22%3A5%2C%22useDefaultActor%22%3Afalse%2C%22__relay_internal__pv__FBReelsEnableDeferrelayprovider%22%3Atrue%7D&server_timestamps=true&doc_id=5168727383225407'
    # payload = {}
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=LKWaYBRwyVwIsRkAApoTOP92; datr=LKWaYPFf3n7WNn6vFH3dS2eO; wd=1280x569; dpr=1.5; locale=en_GB; usida=eyJ2ZXIiOjEsImlkIjoiQXJmOWJ5czExdmhiaHIiLCJ0aW1lIjoxNjU4MjE2NDA0fQ%3D%3D; c_user=100007288237916; xs=35%3AqB6YVlyaXyCIiQ%3A2%3A1658216990%3A-1%3A4199; fr=06rOg5lCaYNKNcGSK.AWVJQDL8M1JVmBjRGnKP4jKG7Mc.Bi1Sd7.zC.AAA.0.0.Bi1mIf.AWXsgvh3XpY; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1658217263366%2C%22v%22%3A1%7D',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/hashtag/{searchKeyword}',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'viewport-width': '544',
        'x-fb-friendly-name': 'SearchCometInterestsDeepDivePostsListQuery',
        'x-fb-lsd': '1-ESj1NwWFjYAzT89bQKNy'
       
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # for items in response.json():
    #     print(items)
    fb = response.json()['data']
    print(fb)
    return "hello"
'''

{"data":{"topic_deep_dive":{"rendering_strategies":{"edges":[{"rendering_strategy":{"__typename":"ExploreErrorRenderingStrategy","explore_view_model":{"__typename":"ExploreErrorViewModel","error_state":"EMPTY_RESULT_PAGE"}},"cursor":"0","node":{"__typename":"ExploreErrorRenderingStrategy"}}],"page_info":{"end_cursor":null,"has_next_page":false}}}},"extensions":{"fulfilled_payloads":[{"label":"SearchCometInterestsDeepDivePostsListQuery_query$defer$SearchCometInterestsDeepDivePostsListQuery_rendering_strategies$page_info","path":["topic_deep_dive","rendering_strategies"]}],"is_final":true}}

message_container->story->message
styles->attachment->media->photo_image->uri
'''

def fetch_by_keyword(searchKeyword):
    fb_post = fb_data(searchKeyword)
    data = []
    data.append(fb_post)
    # for key in fb_post:
    #     data.append({
    #         'post_url': fb_post[key]['entities']['media'][0]['expanded_url'],
    #         'image_url': fb_post[key]['entities']['media'][0]['media_url'],
    #         'likes': fb_post[key]['favorite_count'],
    #         # 'retweets': tweets[key]['retweet_count'],
    #         # 'replies': tweets[key]['reply_count'],
    #         'description': fb_post[key]['full_text']
    #     })
    return json.dumps(data)
    

@facebook.route('/query=<searchKeyword>', methods=['GET'])
def get_facebook_keyword(searchKeyword):
    return fetch_by_keyword(searchKeyword)
