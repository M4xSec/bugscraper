from bs4 import BeautifulSoup
import requests
import urllib
import json
import argparse
import datetime
import os
from platform import system

def banner():

    print('''\033[31m  
    ▄▄▄▄    █    ██   ▄████   ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███    
   ▓█████▄  ██  ▓██▒ ██▒ ▀█▒▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
   ▒██▒ ▄██▓██  ▒██░▒██░▄▄▄░░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
   ▒██░█▀  ▓▓█  ░██░░▓█  ██▓  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
   ░▓█  ▀█▓▒▒█████▓ ░▒▓███▀▒▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ░▒▓███▀▒░▒▓▒ ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ▒░▒   ░ ░░▒░ ░ ░   ░   ░ ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░         
                    \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
                    \`-'  /    `-._  "       "  _.-'    \  `-'/
                    /)   (         \    ,-.    /         )   (\.
                 ,-'"     `-.       \  /   \  /       .-'     "`-,
               ,'_._         `-.__@_/ /  _  \ \__@_.-'         _._`,
              /,'   `.                \_/ \_/                .'   `,\.
             /'       )                  _                  (       `\.
                     /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \.
                     / ,-'        \/|`|`|`|'|'|'|\/        `-, \.
                    /,'             | | | | | | |             `,\.
                                     ` | | | '
                                        ` | '    \033[00m 
\033[00m                  \033[01m\033[33m         >>> cOdEd By: Predator0x300 <<<\033[00m\033[00m
\033[01m\033[33m              >>>--- GitHub:\033[31m  https://github.com/Predator0x300 \033[00m\033[33m ---<<<\033[00m\033[00m\n''')
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

os.system("clear")

max_dictionary =''
def myurl(query, count='10'):
    global url
    url = "https://medium.com/search/posts?q="+urllib.parse.quote(query)+"&count="+count

def do_medium():
    global max_dictionary
    myurl(query, count)
    os.system("clear")
    print("\033[32m{+} Searching %s Articles on Medium.....\033[00m\n" %count)
    try:
        page = requests.get(url)
    except requests.ConnectionError:
        print("\033[32m{-} Failed To Connect! Check Your Connection!\033[00m")
        exit()

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(page.content)
    for divs in soup.find_all('div', class_='postArticle-content'):
        for anchors in divs.find_all('a'):
            for h3 in anchors.find_all('h3'):
                try:

                    max_dictionary += "-"*70 + "\n" + h3.contents[0] + ": " + anchors['href'] + "\n"
                except:
                    pass
    print(max_dictionary)

argp = argparse.ArgumentParser(usage = 'bugscraper.py -t hackerone -q "sql injection" -c [COUNT] -o [File.txt]')
banner()
argp.add_argument("-t","--type",required= True)
argp.add_argument("-q","--query",required= True)
argp.add_argument("-c","--count")
argp.add_argument("-o","--output")
parser = argp.parse_args()
type = parser.type
query = parser.query
count = parser.count
output = parser.output
if(count == None): count = '20'

def do_hackerone():

    global query
    global max_dictionary
    query_ql=r"""
    {"operationName":"HacktivityPageQuery","variables":{"querystring":"%s","where":{"report":{"disclosed_at":{"_is_null":false}}},"orderBy":{"field":"popular","direction":"DESC"},"secureOrderBy":null,"count":%s,"maxShownVoters":10,"cursor":"MTI1"},"query":"query HacktivityPageQuery($querystring: String, $orderBy: HacktivityItemOrderInput, $secureOrderBy: FiltersHacktivityItemFilterOrder, $where: FiltersHacktivityItemFilterInput, $count: Int, $cursor: String, $maxShownVoters: Int) {\n  me {\n    id\n    __typename\n  }\n  hacktivity_items(first: $count, after: $cursor, query: $querystring, order_by: $orderBy, secure_order_by: $secureOrderBy, where: $where) {\n    total_count\n    ...HacktivityList\n    __typename\n  }\n}\n\nfragment HacktivityList on HacktivityItemConnection {\n  total_count\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  edges {\n    node {\n      ... on HacktivityItemInterface {\n        id\n        databaseId: _id\n        ...HacktivityItem\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HacktivityItem on HacktivityItemUnion {\n  type: __typename\n  ... on HacktivityItemInterface {\n    id\n    votes {\n      total_count\n      __typename\n    }\n    voters: votes(last: $maxShownVoters) {\n      edges {\n        node {\n          id\n          user {\n            id\n            username\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    upvoted: upvoted_by_current_user\n    __typename\n  }\n  ... on Undisclosed {\n    id\n    ...HacktivityItemUndisclosed\n    __typename\n  }\n  ... on Disclosed {\n    id\n    ...HacktivityItemDisclosed\n    __typename\n  }\n  ... on HackerPublished {\n    id\n    ...HacktivityItemHackerPublished\n    __typename\n  }\n}\n\nfragment HacktivityItemUndisclosed on Undisclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  requires_view_privilege\n  total_awarded_amount\n  currency\n  __typename\n}\n\nfragment TeamLinkWithMiniProfile on Team {\n  id\n  handle\n  name\n  __typename\n}\n\nfragment UserLinkWithMiniProfile on User {\n  id\n  username\n  __typename\n}\n\nfragment HacktivityItemDisclosed on Disclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    title\n    substate\n    url\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  total_awarded_amount\n  severity_rating\n  currency\n  __typename\n}\n\nfragment HacktivityItemHackerPublished on HackerPublished {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    id\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    url\n    title\n    substate\n    __typename\n  }\n  latest_disclosable_activity_at\n  severity_rating\n  __typename\n}\n"}
    """ % (query, int(count))
    print("\033[32m {+} Searching %s Articles on Hackerone.....\033[00m\n" %count)
    headers = {"content-type": "application/json"}

    try:
        request = requests.post('https://hackerone.com/graphql', data=query_ql, headers=headers)
    except requests.ConnectionError:
        print("\033[32m{-} Failed To Connect! Check Your Connection!\033[00m")
        exit()

    if request.status_code == 200:

        json_response = json.loads(json.dumps(request.json()))

        if not len(json_response['data']['hacktivity_items']['edges']):
            print("\033[32m{~} Failed To Savage!\033[00m")
            exit()
        for i in range(len(json_response['data']['hacktivity_items']['edges'])):
            try:
                max_dictionary +=  "{~}"+"-"*70 + "\n" + json_response['data']['hacktivity_items']['edges'][i]['node']['report']['title'] +": " + json_response['data']['hacktivity_items']['edges'][i]['node']['report']['url'] + "\n"
            except:
                pass
        print(max_dictionary)
    else:
        raise Exception("\033[32mQuery failed to run by returning code of {}. {}\033[00m".format(request.status_code, request.headers))

do_medium() if(type == 'medium') else do_hackerone()

if(output):
    try:
        file = open(output,"w", encoding= "UTF-8")
        file.write("{+} Bugscraper Scan Results at %s" %datetime.datetime.now()+"\n\n")
        file.write("{+} Query: %s for %s results from %s\n\n" %(query, count, type))
        file.write(max_dictionary)
        file.close()
        print("\033[32m{+} Output written to file %s\033[00m\n" %output)
    except FileExistsError:
        print("\033[32mFile doesn't Exist! :(\033[00m")
    except IOError:
        print("\033[32mWriting to file failed! ;(\033[00m")