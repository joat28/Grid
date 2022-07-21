from flask import Blueprint, jsonify
import json
import requests
import http.client
import re
facebook = Blueprint('facebook', __name__, url_prefix='/facebook')

#?sorting_setting=CHRONOLOGICAL&source=lhc&ref=nf

def fb_data(searchKeyword):
    searchKeyword = str(searchKeyword)
    #searchKeyword = "https://www.facebook.com/search/top/?q=" + searchKeyword
    conn = http.client.HTTPSConnection("www.facebook.com")
    payload = f'av=100007288237916&__user=100007288237916&__a=1&__dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU29gS3q2ibwyzE2qwJxS1NwJwpUe8hw47w5nCxS320om782Cwwwqo465o-cwfG12wOKdwGxu782ly87e2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzEjxq1jxS6FobrwKxm5oe8464-5pUfEdK1EDBx_y88E3VBwJCwLyESE2KwwwOhE25wMwhF8-4UdUcojxK&__csr=gk82bcPijjT4RlQRO9ijEGtQynFYzEBtl4OiGVmGl5F9fl4mLGWhkhrlLvWhyAWK8UwKHAVqFBQAmF8BpaADCy-8yB8KaBhemqaABBzUKh6wyAWUg-Am8yta4F8gx7yoW9wRyByoWaUhDzE98fUGaK7UC5o6i1mAUC1ygbo7Cq1wwTwqu1FxK2K0QU6e10wZxy6o15FU3XDx60nq06lk02aq0q206zGw08ym0cUw4exi7Ey2Tw4Hw3dd01cii3CE1wE0M21lw0yxwcW019aw&__req=28&__hs=19194.HYP%3Acomet_plat_default_pkg.2.1.0.2.0&dpr=1.5&__ccg=GOOD&__rev=1005885592&__s=q0unls%3A37nf8z%3Ae7s5q4&__hsi=7122716606955618399&__comet_req=1&fb_dtsg=NAcPVRJdHpeC7xJqGpEvozEPQylkY2IeBBdu09vmGAaEW6DjUIA7F8g%3A33%3A1658386628&jazoest=25416&lsd=19Vo7CIfxDdFmnsKhGj8xi&__spin_r=1005885592&__spin_b=trunk&__spin_t=1658386692&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=SearchCometInterestsDeepDivePostsListQuery&variables=%7B%22UFI2CommentsProvider_commentsKey%22%3A%22SearchCometInterestsDeepDiveRootQuery%22%2C%22displayCommentsContextEnableComment%22%3Afalse%2C%22displayCommentsContextIsAdPreview%22%3Afalse%2C%22displayCommentsContextIsAggregatedShare%22%3Afalse%2C%22displayCommentsContextIsStorySet%22%3Atrue%2C%22displayCommentsFeedbackContext%22%3Anull%2C%22feedLocation%22%3A%22SEARCH%22%2C%22feedbackSource%22%3A40%2C%22focusCommentID%22%3Anull%2C%22input%22%3A%7B%22extra_data%22%3A%22%7B%5C%22entry_point%5C%22%3A4%7D%22%2C%22scope_information%22%3Anull%2C%22session_id%22%3A%22ff484422-aebf-4e29-8c71-9f55b4a323da%22%2C%22topic_id%22%3A%22%23{searchKeyword}%22%2C%22explore_tab%22%3A%22TOP%22%7D%2C%22locale%22%3Anull%2C%22privacySelectorRenderLocation%22%3A%22COMET_STREAM%22%2C%22renderLocation%22%3A%22search_results_page%22%2C%22scale%22%3A1.5%2C%22topic_results_paginating_after_cursor%22%3A%22%7B%5C%22current_section%5C%22%3A12%2C%5C%22serialized_section_cursor%5C%22%3A%5C%22%7B%5C%5C%5C%22serialized_browse_cursor%5C%5C%5C%22%3A%5C%5C%5C%22AbrN81x1uWvS7f5fFSqLLK-8gVwcy0CRJFR9URaAqPbbWvCNAbve1Z2j7x5VXTTYz0Yu451zZP_0V0o7azpsGVRnbvvZOHF1pXXBqhJeO16X_OO5K6yvyNM81kJNfCwQs71bX8sP7ggM319S6Vh2UQ9NeI1LhsK8CYH3bKNqYpVvuo0RNpob-RHGG0PnpBx2JzJHfrvDvPliY9atrE4D5IVYxBnX75ITz1l1HpOs6BlUo5H4IQWkZqPoPYUHZ7Ad_fyqyBU0l4Ua5581VEacwP-DyYjLx207Hm0FRVA0yNpjgxZS1np9Llw8XMwssql3qVsdxuRRGcag0CZHWSBepAukroazQJJvcJXY8rJ0mH6_SGEtclM38DjCP2q4bccNfVsyxSwYkRHK_xIUz77kVcL4kVecE8rykKM8uDi4APBDBKbPqsr_BYB6AiZog0v6crzcVvOotZ2--zIKf7Bdih_783xH6F3Z4CYIUHW_9_5I9WHxoKHltPpl9hTWwgPUl6wfsrvagNDCxQSqNw1rEICMuE8EjI6-9Ac6FBI9urQmJ7yUXGB0KKUmwLRCuWHl_rZjG-zJF0LDrh_Zdd6OKNd2SVXw946XMnsU-gRWO3feaA%5C%5C%5C%22%2C%5C%5C%5C%22browse_unit_id%5C%5C%5C%22%3A%5C%5C%5C%22browse_serp%3Ae0fd7121-aaab-4387-b5bd-5e42fb4fb9e1%5C%5C%5C%22%2C%5C%5C%5C%22top_n_fbids_shown_at_start_of_section%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22session_id%5C%22%3A%5C%22ff484422-aebf-4e29-8c71-9f55b4a323da%5C%22%2C%5C%22current_page_num%5C%22%3A1%2C%5C%22section_to_num_results_shown%5C%22%3A%7B%5C%22top_posts%5C%22%3A2%7D%2C%5C%22top_n_fbids_shown%5C%22%3A%5B106091233641167%2C358339432324821%5D%2C%5C%22quick_promotion_fbids_shown%5C%22%3A%5B%5D%7D%22%2C%22topic_results_paginating_at_stream_enabled%22%3Afalse%2C%22topic_results_paginating_at_stream_initial_count%22%3A1%2C%22topic_results_paginating_first%22%3A5%2C%22useDefaultActor%22%3Afalse%2C%22__relay_internal__pv__FBReelsEnableDeferrelayprovider%22%3Atrue%7D&server_timestamps=true&doc_id=5197318153715437'
    headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'sb=LKWaYBRwyVwIsRkAApoTOP92; datr=LKWaYPFf3n7WNn6vFH3dS2eO; dpr=1.5; locale=en_GB; wd=562x569; c_user=100007288237916; xs=33%3AZeSFCmhvggPLCg%3A2%3A1658386628%3A-1%3A4199; fr=0LVdS3KICtRMrXS1N.AWUNFxnRRGsPNTVU52cDTc_5nuo.Bi2N-F.zC.AAA.0.0.Bi2PjE.AWWFG_IobiM; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1658386698936%2C%22v%22%3A1%7D',
    'origin': 'https://www.facebook.com',
    'referer': f'https://www.facebook.com/hashtag/{searchKeyword}',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'viewport-width': '562',
    'x-fb-friendly-name': 'SearchCometInterestsDeepDivePostsListQuery',
    'x-fb-lsd': '19Vo7CIfxDdFmnsKhGj8xi'
    }
    conn.request("POST", "/api/graphql/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    #print(data.decode("utf-8"))
    return data.decode("utf-8")



def fetch_by_keyword(searchKeyword):
    fb_post = fb_data(searchKeyword)
    
    # print(fb_post)
    data = fb_post.replace("\"", "")
    data = data.replace("\\", "")
    data = data[1:-2]
    data = data.split("},")
    
    store = []
    for key in data:
        url_sets = set()
        if key.find("https") != -1:
            key = key.split("https")
            for i in range(len(key)):
                if i == 0:
                    continue
                key[i] = "https" + key[i]
                url_sets.add(key[i])
            for items in url_sets:
                url = items.split(",")[0]
                if(url.find("jpg") != -1 or url.find("png") != -1 or url.find("jpeg") != -1):
                    store.append(url)
                
    store = list(set(store))
        
    return json.dumps(store)
    

@facebook.route('/query=<searchKeyword>', methods=['GET'])
def get_facebook_keyword(searchKeyword):
    return fetch_by_keyword(searchKeyword)
