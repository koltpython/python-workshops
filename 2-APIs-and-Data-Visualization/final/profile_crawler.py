import requests


def get_follow_and_visibility_data(usernames):

    public_usernames = []
    follow_statistics = {}

    for username in usernames:
        user_url = f'https://www.instagram.com/{username}/?__a=1'
        user_response = requests.get(user_url).json()['graphql']['user']

        if not user_response['is_private']:
            public_usernames.append(username)

        follow_count = user_response['edge_follow']['count']
        follower_count = user_response['edge_followed_by']['count']
        follow_statistics[username] = (follow_count, follower_count)

    return (follow_statistics, public_usernames)


def get_post_data(public_usernames):
    photos = []
    for username in public_usernames:
        user_url = f'https://www.instagram.com/{username}/?__a=1'
        user_response = requests.get(user_url).json()['graphql']['user']
        # response has the latest 12 (or less) post of user
        posts = user_response['edge_owner_to_timeline_media']['edges']
        for post in posts:
            photos.append(
                (post['node']['display_url'], post['node']['edge_liked_by']['count'], username))

    photos.sort(key=lambda post: post[1], reverse=True)
    return photos
