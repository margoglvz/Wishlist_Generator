import json
import urllib.parse
import urllib.request

EBAY_API_TOKEN = 'Bearer v^1.1#i^1#p^1#r^0#f^0#I^3#t^H4sIAAAAAAAAAOVYbWwURRjutVeEIkL4qqAk5xZTQ7m9/bi93i29g+Ou0EppS6+ltKJ0P2Z7a+92tztzXIsSaiMQIAFjolH5U+MnmoBWkIraJqZqQGL0hyb+ghABwY9oJEIiEGe3pVwr4auX2MT7c5l33nnneZ5535nZobomTVm0rWLbxWmOe3J7uqiuXIeDnkpNmZRfcl9e7vz8HCrDwdHTtbDL2Z33UxkUkgmDrwPQ0DUIXB3JhAZ52xgkUqbG6wJUIa8JSQB5JPGx8OoqniEp3jB1pEt6gnBVRoMEkBiaoktlzidwnCLL2Kpdi1mvBwmpVGYVv0AHRE70AU7A/RCmQKUGkaChIMFQDOumaTftq6dYnmZ4hiUDnK+ZcK0FJlR1DbuQFBGy4fL2WDMD682hChACE+EgRKgyvCJWE66MllfXl3kyYoWGdYghAaXg6FZEl4FrrZBIgZtPA21vPpaSJAAh4QkNzTA6KB++BuYu4NtSexVGkbGWkqIAKSBKWZFyhW4mBXRzHJZFld2K7coDDamo81aKYjXEJ4GEhlvVOERl1GX9rUkJCVVRgRkkypeHm8K1tURopSlIIBJX3Y0qjJvu2rqoOyD5/X5F8tJuzi8GKEb2Ds8yFGpY4zHTRHRNVi3FoKtaR8sBhgzGCkNlCIOdarQaM6wgC06mH3dNQG9ps7WiQ0uYQnHNWlSQxCq47Oat5R8ZjZCpiikERiKM7bD1CRKCYagyMbbTTsTh3OmAQSKOkMF7POl0mkyzpG62ehiKoj3rVlfFpDhI4kqzfa1ax/7qrQe4VZuKBPBIqPKo08BYOnCiYgBaKxHy+rlSb+mw7qNhhcZa/2XI4OwZXQ7ZKg9ZZGQaBJSAyCgix2alPELDGeqxcABR6HQnBbMNICOB89Ut4TxLJYGpyjzLKQzrV4Bb9gUUtzegKG6Rk31uWgGAAkAUpYD/f1Mlt5vnMSCZAGUr0bOT5K3lpSWBeJ2+vMbfmWjzVSfTjWnfmqpHaxrDG/2rzE3RKqW2IhJHjNIQvN1SuCH5SELFytTj+bMngFXr2RChQocIyOOiF5N0A9TqCVXqnFgLzJpyrWCizhhIJLBhXCTDhlGZtY06O/TuZI+4O9JZPZ3+i5Pphqygla8Ti5U1HuIAgqGS1tlDSnrSowv40mGZrFrfYKMeF28VX1gnFGtMcoitKg/dNEmbMgk3SqQJoJ4y8SWbrLHuXvV6G9DwYYZMPZEA5lp63MWcTKaQICbARKvqLCS4Kkywk5Yuxe6Ul/Wy4+Il2efohom2JWV1H3YuuYPbtGf0h30ox/7R3Y7PqG5Hf67DQZVRD9NF1EOT8hqceffOhyoCpCooJFRbNfy9agKyDXQagmrmzsq5SJ3dK/1SsW9n29V0+5klm3My3xV6HqfuH3lZmJJHT814ZqAevN6TT08vnMawNE37KJZmGLaZKrre66TnOmc31F06uNN0PXBi29vvtCQnX3lkyeUPqWkjTg5Hfo6z25Hj4Cqu9jQsvbw0/YyTPD/wZfHC72L7Ihs7mou3XiiveqPkz672aP3JFU3MU31bPh/c//sy+eV5RR+wh/u+reY+re57obXr18nF+xeU/ziv96u9hw/tUHa/m3ulLAde2vXDQWLLnhfVvue/7zswG77f2FJy/KXKQf+cwa/XR/cXzip87hSa17Blz8cbijZPf22V87E5b6ZnnHmiIDA98kXd61xL5OjWT3ade8vY0fRsvPb4kSPbBwp7N5UF21v6Zyw7eY75beDVY8Wzvznw89m/Tiw4dWLmot73ThfQ3U8PDiTXFRfM7Y/O1MTFu496Vjaf/8N/4Uhq75pX1hunc12grCnd0LujqL1g8bFDf3/UP7SW/wDpg91L8REAAA=='

BASE_EBAY_URL = 'https://api.ebay.com/buy/browse/v1/item_summary'

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
            headers = {"Authorization":f'{EBAY_API_TOKEN}',
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



def run() -> None:
##    search_query = input('Query: ')
    result = get_result(build_search_url('strawberry', 3))
    print_title_and_description(result)



if __name__ == '__main__':
    run()
