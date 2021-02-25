import requests, json

class api:
    def __init__(self):
        '''
        Fedsearch API by HellSec
        '''

    def search(self, key, query):
        r = requests.post('https://fedsearch.cf/API/search_api.php', data={'search': query, 'submit': '', 'key': key,}).text
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
        r = requests.post('https://fedsearch.cf/API/records.php', data={'key': key, 'submit': ''}).text
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
        r = requests.post('https://fedsearch.cf/API/version.php', data={'key': key, 'submit': ''}).text
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
