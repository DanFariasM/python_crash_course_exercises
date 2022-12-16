from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, discussion_links, discussion_comments = [], [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    
    # Had to include a try-except block because for some reason,
    # one article did not have a "descendants" key. (No ref in the book)
    try:
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"],
        }
    except KeyError:
        pass
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"),
                    reverse=True)

for submission_dict in submission_dicts:
    discussion_name = submission_dict['title']
    print(f"\nTitle: {discussion_name}")

    discussion_url = submission_dict['hn_link']
    print(f"Discussion link: {discussion_url}")
    discussion_link = f"<a href='{discussion_url}'>{discussion_name}</a>"
    discussion_links.append(discussion_link)

    print(f"Comments: {submission_dict['comments']}")
    discussion_comments.append(submission_dict['comments'])

# Make the visualization.
data = [{
    "type": "bar",
    "x": discussion_links,
    "y": discussion_comments,
    "hoverlabel": {"bgcolor": "white"},
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
    },
    "opacity": 0.6,
}]

my_layout = {
    "title": "Active Discussions in Hacker News",
    "title_x": 0.5,
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="ex_17_2_active_discussions.html")