import json
import urllib.parse
import urllib.request
import base64

import requests

ebay_api_token = None
BASE_EBAY_URL = 'https://api.ebay.com/buy/browse/v1/item_summary'

def get_access_token() -> None:
    '''Makes a grant request and gets the access token.'''
    response = None
    try:
        request_body = urllib.parse.urlencode({'grant_type':'client_credentials',
                                                'scope':'https://api.ebay.com/oauth/api_scope'}).encode()
        b = base64.b64encode('GraceChi-Wishr-PRD-9c888fc41-58b902d4:PRD-c888fc4121b6-34ae-4ee4-b239-5694'.encode('utf-8')).decode('utf-8')
        request = urllib.request.Request(
            url = 'https://api.ebay.com/identity/v1/oauth2/token',
            headers = {'Content-Type':'application/x-www-form-urlencoded',
                       'Authorization':'Basic '+b}, 
            data = request_body,
            method = 'POST')
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        json_dict = json.loads(json_text)
        return json_dict['access_token']
        
    finally:
        if response != None:
            response.close()


def build_search_url(search_query: str, limit: int) -> str:
    '''This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    eBay item_summary API for information about products matching the search 
    request.
    '''

    query_parameters = [
        ('q', search_query), ('limit', str(limit)),
    ]

    return f'{BASE_EBAY_URL}/search?{urllib.parse.urlencode(query_parameters)}'

assert build_search_url('strawberry', 3) == 'https://api.ebay.com/buy/browse/v1/item_summary/search?q=strawberry&limit=3'

def get_result(url: str) -> dict:
    '''This function takes a URL and returns a Python dictionary representing
    the parsed JSON response.
    '''
    response = None

    try:
        request = urllib.request.Request(
            url,
            headers = {"Authorization":f'Bearer {ebay_api_token}',
                       "X-EBAY-C-MARKETPLACE-ID":"EBAY_US"})
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()



def print_title_and_description(search_result: dict) -> None:
    '''This function takes a parsed JSON response from the eBay item_summary API's
    search request and prints the title, price, and image url of all of the products
    in the response.
    '''
    for item in search_result['itemSummaries']:
        print(item['title'])
##        print(item['currentBidPrice']['value'])
        print(item['image']['imageUrl'])
        print()



def run(query:str) -> None:
##    search_query = input('Query: ')
##    while True:
##        try:
##            result = get_result(build_search_url('strawberry', 3))
##            print_title_and_description(result)
##            break
##        except:
##            ebay_api_token = get_access_token()
    ebay_api_token = get_access_token()
    # print(ebay_api_token)
    # result = get_result(build_search_url('strawberry', 3))
    # print_title_and_description(result)

        
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

    querystring = {"q":query}

    payload = ""
    headers = {
        "User-Agent": "insomnia/8.4.0",
        "Authorization": "Bearer "+ebay_api_token
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # with open('result.json', 'w') as f:
    #     json.dump(response.json(), f)

    return response.json()




if __name__ == '__main__':
    run('')
