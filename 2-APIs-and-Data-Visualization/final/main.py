import image_show
import username_crawler
import data_visualizer
import profile_crawler

# usernames = username_crawler.get_usernames_from_names('names.txt')
# username_crawler.write_usernames_to_file(usernames)

usernames = username_crawler.read_usernames_from_file('usernames.txt')

follow_statistics, public_usernames = profile_crawler.get_follow_and_visibility_data(
    usernames)

data_visualizer.show_follow_follower_plot(follow_statistics)

data_visualizer.show_bar_graph(('private', 'public'), (len(
    usernames)-len(public_usernames), len(public_usernames)), 'Profile Visibility')

posts_sorted_by_likes = profile_crawler.get_post_data(public_usernames)

top_50_posts = posts_sorted_by_likes[:50]
top_50_likes = [post[1] for post in top_50_posts]
top_50_usernames = []

top_post_count = {}

for post in top_50_posts:
    if post[2] in top_post_count:
        top_50_usernames.append(f'{post[2]}-{top_post_count[post[2]]}')
        top_post_count[post[2]] += 1
    else:
        top_post_count[post[2]] = 1
        top_50_usernames.append(post[2])

data_visualizer.show_bar_graph(top_50_usernames, top_50_likes, 'Top 50 Posts')

# Show the most liked post
image_show.show_img_from_url(posts_sorted_by_likes[0][0])
