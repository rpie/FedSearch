import requests, json

class api:
    def __init__(self):
        '''
        Fedsearch v1 by HellSec And Nano
        '''

    def search(self, key, query):
        r = requests.get('https://fedsearch.cf/API/search_api.php', headers={'key': key, 'search': query, 'submit': ''}).text
        if 'DOCTYPE' in r:
            error = f'\033[31m[Error]\033[0m Cloudflare Ratelimit'
            return(error)
        elif 'Blocked' in r:
            error = f'\033[31m[Error]\033[0m Blocked By Cloudflare'
            return(error)
        elif 'Dirrect' in r:
            error = f'\033[31m[Error]\033[0m Dirrect Access Error'
            return(error)
        else:
            return(r)

    def records(self, key):
        r = requests.get('https://fedsearch.cf/API/records.php', headers={'key': key, 'submit': ''}).text
        if 'DOCTYPE' in r:
            error = f'\033[31m[Error]\033[0m Cloudflare Ratelimit'
            return(error)
        elif 'Blocked' in r:
            error = f'\033[31m[Error]\033[0m Blocked By Cloudflare'
            return(error)
        elif 'Dirrect' in r:
            error = f'\033[31m[Error]\033[0m Dirrect Access Error'
            return(error)
        else:
            return(r)

    def version(self, key):
        r = requests.get('https://fedsearch.cf/API/version.php', headers={'key': key, 'submit': ''}).text
        if 'DOCTYPE' in r:
            error = f'\033[31m[Error]\033[0m Cloudflare Ratelimit'
            return(error)
        elif 'Blocked' in r:
            error = f'\033[31m[Error]\033[0m Blocked By Cloudflare'
            return(error)
        elif 'Dirrect' in r:
            error = f'\033[31m[Error]\033[0m Dirrect Access Error'
            return(error)
        else:
            return(r)
