import requests


def get_follow_and_visibility_data(usernames):

    public_usernames = []
    follow_statistics = {}

    # TODO: create follow statistics dictionary username -> (follow, follower)
    # and public usernames list

    return (follow_statistics, public_usernames)


def get_post_data(public_usernames):
    photos = []

    # TODO: get posts of public users
    # posts are represented as tuple of (display_url, like_count, username)

    # Sort the photos link by like count in descending order
    photos.sort(key=lambda post: post[1], reverse=True)
    return photos
