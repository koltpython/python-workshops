import matplotlib.pyplot as plt


def show_follow_follower_plot(follow_statistics):
    follows = []
    followers = []
    for username in follow_statistics:
        follows.append(follow_statistics[username][0])
        followers.append(follow_statistics[username][1])

    fig, ax = plt.subplots()
    min_data = min(min(follows), min(followers))
    max_data = max(max(follows), max(followers))

    # gca is an abbreviation "get the current axes"
    axes = plt.gca()
    axes.set_xlim([min_data, max_data])
    axes.set_ylim([min_data, max_data])
    axes.set_xlabel('Follow')
    axes.set_ylabel('Follower')

    plt.scatter(follows, followers)

    for username in follow_statistics:
        plt.annotate(username, follow_statistics[username])

    plt.show()


def show_bar_graph(labels, values, title=''):
    if title:
        plt.title(title)
    plt.bar(labels, values)
    if len(labels) > 5:
        plt.xticks(rotation='vertical')
    plt.show()
