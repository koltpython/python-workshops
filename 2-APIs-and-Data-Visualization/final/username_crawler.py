import requests
import urllib.parse


def get_usernames_from_names(name_file):
    usernames = []

    with open(name_file, mode='r', encoding='utf-8') as names_file:
        for line in names_file:
            query = line.strip()
            query_encoded = urllib.parse.quote(query)

            search_url = f'https://www.instagram.com/web/search/topsearch/?query={query_encoded}'
            response = requests.get(search_url)
            data = response.json()

            if data and 'users' in data and data['users']:
                username = data['users'][0]['user']['username']
                usernames.append(username)

    return usernames


def write_usernames_to_file(usernames):
    with open('usernames.txt', 'x') as usernames_file:
        usernames_file.write('\n'.join(usernames))


def read_usernames_from_file(username_file):
    usernames = []
    with open(username_file, 'r') as usernames_file:
        for username in usernames_file:
            usernames.append(username.strip())
    return usernames
