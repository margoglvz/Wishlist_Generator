import json
import urllib.parse
import urllib.request

EBAY_API_KEY = 'INSERT KEY HERE'

BASE_EBAY_URL = 'https://api.ebay.com/buy/browse/v1/item_summary'

def build_search_url(search_query: str, limit: int, filter: list[str]) -> str:
    '''This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    eBay item_summary API for information about products matching the search 
    request.
    '''

    query_parameters = [
        ('q', search_query), ('key', EBAY_API_KEY), ('limit', str(limit)),
    ]

    return f'{BASE_YOUTUBE_URL}/search?{urllib.parse.urlencode(query_parameters)}'



def get_result(url: str) -> dict:
    '''This function takes a URL and returns a Python dictionary representing
    the parsed JSON response.
    '''
    response = None

    try:
        request = urllib.request.Request(url)
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
        print(item['shortDescription'])
        print(item['currentBidPrice']['value'])
        print(item['image']['imageUrl'])
        print()



def run() -> None:
    search_query = input('Query: ')
    result = get_result(build_search_url(search_query, 10))
    print_title_and_description(result)



if __name__ == '__main__':
    run()