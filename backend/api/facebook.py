from flask import Blueprint, jsonify
import json
import requests

facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

#?sorting_setting=CHRONOLOGICAL&source=lhc&ref=nf

def fb_data(searchKeyword):
    url = "https://www.facebook.com/api/graphql/"
    payload = 'av=100007288237916&__user=100007288237916&__a=1&__dyn=7AzHK4HwkEng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o11U1lVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782ly87e2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUws9ovUy2a0-pobpEbUGdG0HE88cAq0xoc84qifxe3u364Urw&__csr=g_b3QmBd4sIYmG4ijiTOn5QzWplTqYFGpnnlnsG9tdGmjAGKJ8SLiLjl4WhajmivADByqiQuAi9CGF9FpmqKuifKEPAyoK8y8CiVGz94qayemGyF_yQ8xzALyqADxueADhbxKcFogxiiaBZ3U-udg6G2qbxu78G58c8O22fDUJ3VEowwxm69Ua8y263KfwiUG5E_yo8V-3CdxN0yx-0x8dogxe58y2Sbx63W32p0qE9K2i0hJ0uo5q0EU24wcC02Yq06WU980mOg9E7Dw08XBw4Ww7Tg0kZw8Cawb205fU0jlw9S1Ez8igjw1jNxm07LE1A80opw&__req=2&__hs=19192.HYP%3Acomet_pkg.2.1.0.2.0&dpr=1.5&__ccg=EXCELLENT&__rev=1005869239&__s=781t65%3A8ap0nv%3A9yy2ka&__hsi=7122017150303210296&__comet_req=15&fb_dtsg=NAcPgFC_bXlxluc8qXK8TwYdLtDeqSrkzu5z7rfKC_6whybTETD5dIA%3A48%3A1658220098&jazoest=25712&lsd=-1mysNLksQ5eP_IuNPSgeL&__spin_r=1005869239&__spin_b=trunk&__spin_t=1658223837&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometInterestsDeepDivePostsListQuery&variables=%7B%22UFI2CommentsProvider_commentsKey%22%3A%22SearchCometInterestsDeepDiveRootQuery%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Atrue%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22feedLocation%22%3A%22SEARCH%22%2C%22feedbackSource%22%3A40%2C%22focusCommentID%22%3Anull%2C%22input%22%3A%7B%22extra_data%22%3Anull%2C%22scope_information%22%3Anull%2C%22session_id%22%3A%223cdb55a4-8587-4bfb-ac10-cd31c74dd17e%22%2C%22topic_id%22%3A%22%23{searchKeyword}%22%2C%22explore_tab%22%3A%22TOP%22%7D%2C%22locale%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22search_results_page%22%2C%22scale%22%3A1.5%2C%22topic_results_paginating_after_cursor%22%3A%22%7B%5C%22current_section%5C%22%3A12%2C%5C%22serialized_section_cursor%5C%22%3A%5C%22%7B%5C%5C%5C%22serialized_browse_cursor%5C%5C%5C%22%3A%5C%5C%5C%22AbrYvl6DoiO42mJToENwwH7nujmBcKELJYPSuYYSgj77NCs8PVhd1aly9p_PWNJxQ8iZNRYM6_c-GQNVq_6upT_y66bzo9LVSUBfobh2IVnCeNVIYPQpGnnOynRqV1HwT3tAWM3f-ZLr9iAnnCHKvNFV4uNY-kQe9PNsEZfnlYJ1qekmgEovNFHVlPOj3qzcr-J9G06tE5iSHPl2dl3loPnmBIdPHeWf5eznhvCpRxCnsyQqBujjZ7yrJLF4PKwcDaD2u5ssF-vKkUaK2-JpJEClBRXzfEb9XKqJnSWAPp4DDSdIkTQYrvrWUQSToD6JGfhXo17NOPyxs2dLteyUWjQcrhIQCJL_JPeN2XCK5kmJ56uJhYDOH0yH5AZ8EnPmcPYhhqwUvrgh7N5nHmYe8ie5BlERQqmcbt-ZminHJMbJBahyKTdIvq-Z_BayLUS1vTQ-ayDxsjgRKIz-bRLjZ4IPO0yxffKUI5pSR8lcEcatDwFC7nuu0CovI2s2NWXm_b2rm-ZeNDNRXQBe2LtsQZ8EIUA0cjQarMQt1JjLc1EKSbEpos44VWMBRVwgSMxpDE4nNoaWvIg49Y3Uf2LtjLafLxwh0y9X-PJpqAJcts-1vQ%5C%5C%5C%22%2C%5C%5C%5C%22browse_unit_id%5C%5C%5C%22%3A%5C%5C%5C%22browse_serp%3Ac51b3cb8-ca25-4f92-b71c-8791a742b3fb%5C%5C%5C%22%2C%5C%5C%5C%22top_n_fbids_shown_at_start_of_section%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22session_id%5C%22%3A%5C%223cdb55a4-8587-4bfb-ac10-cd31c74dd17e%5C%22%2C%5C%22current_page_num%5C%22%3A1%2C%5C%22section_to_num_results_shown%5C%22%3A%7B%5C%22top_posts%5C%22%3A2%7D%2C%5C%22top_n_fbids_shown%5C%22%3A%5B106091233641167%2C358339432324821%5D%2C%5C%22quick_promotion_fbids_shown%5C%22%3A%5B%5D%7D%22%2C%22topic_results_paginating_at_stream_enabled%22%3Afalse%2C%22topic_results_paginating_at_stream_initial_count%22%3A1%2C%22topic_results_paginating_first%22%3A5%2C%22useDefaultActor%22%3Afalse%2C%22__relay_internal__pv__FBReelsEnableDeferrelayprovider%22%3Atrue%7D&server_timestamps=true&doc_id=5168727383225407'


    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=LKWaYBRwyVwIsRkAApoTOP92; datr=LKWaYPFf3n7WNn6vFH3dS2eO; wd=1280x569; dpr=1.5; locale=en_GB; usida=eyJ2ZXIiOjEsImlkIjoiQXJmOWJ5czExdmhiaHIiLCJ0aW1lIjoxNjU4MjE2NDA0fQ%3D%3D; c_user=100007288237916; xs=48%3A2aNSHIy3rPFRxw%3A2%3A1658220098%3A-1%3A4199; fr=06rOg5lCaYNKNcGSK.AWWq84t8Q8oUZ2aO_pQERqtwuWo.Bi1Sd7.zC.AAA.0.0.Bi1m5B.AWURbEB0xTk; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1658220107455%2C%22v%22%3A1%7D',
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
        'x-fb-lsd': '-1mysNLksQ5eP_IuNPSgeL'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # for items in response.json():
    #     print(items)
    fb = (response.text)
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
