import requests, json

class api:
    def __init__(self):
        '''
        Fedsearch API by HellSec
        '''

    def search(self, key, query):
        r = requests.post('https://fedsearch.cf/API/search_api.php', data={'search': query, 'submit': '', 'key': key,}).json()
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

    def prettyprint(self, key, query):
        r = requests.post('https://fedsearch.cf/API/search_api.php', data={'search': query, 'submit': '', 'key': key,}).json()
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
            results = []
            for result in r:
                email, password, ip, token, database = result['email'], result['password'], result['ip'], result['token'], result['database']
                results.append(f'''
                   \033[31m______
\033[31m==================[\033[0mResult\033[31m]==================\033[0m

Email       :   {email}        
Password    :   {password}
Token       :   {token}
IP Address  :   {ip}
Database    :   {database}

\033[31m============================================\033[0m''')
            return(results)
