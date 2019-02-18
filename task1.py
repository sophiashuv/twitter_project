import urllib.request, urllib.error
import twurl
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def table(aspect, js):
    """
    The function takes an aspect and js and returns a dictionary of
    and the information about them in this aspect.
    """
    databace = dict()
    for u in js['users']:
        if aspect in u:
            databace[u["screen_name"]] = u[aspect]
    return databace


def all_aspects(js):
    """
    The function takes js and returns a list of all aspects.
    """
    lst = []
    for u in js['users']:
        lst.append(u.keys())
    return lst


while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '500'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print("Choose one from all aspects")
    print(all_aspects(js))
    print('')
    aspect = input('Enter an aspect:')
    print(table(aspect, js))
