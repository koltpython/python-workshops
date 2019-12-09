import requests
import matplotlib.pyplot as plt

import image_show
import username_crawler

usernames = username_crawler.get_usernames_from_names('names.txt')
username_crawler.write_usernames_to_file(usernames)

# usernames = username_crawler.read_usernames_from_file('usernames.txt')
