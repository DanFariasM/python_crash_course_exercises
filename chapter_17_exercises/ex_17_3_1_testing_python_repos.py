# Re-writing the original file, structured into functions to be tested.

import requests

from plotly.graph_objs import Bar
from plotly import offline

def get_api_response():
    """Make and API call and store the response."""
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers = headers)
    return r

def get_repo_dicts(r):
    """Process results and get a set of dictionaries with repositories."""
    response_dict = r.json()
    repo_dicts = response_dict["items"]
    return repo_dicts

def get_data(repo_dicts):
    """Return the data needed to be represented in the visualization."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict["name"]
        repo_url = repo_dict["html_url"]
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict["stargazers_count"])

        owner = repo_dict["owner"]["login"]
        description = repo_dict["description"]
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    """Generate the visualization of the most commented articles."""
    data = [{
        "type": "bar",
        "x": repo_links,
        "y": stars,
        "hovertext": labels,
        "hoverlabel": {"bgcolor": "white"},
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
        },
        "opacity": 0.6,
    }]

    my_layout = {
        "title": "Most-Starred Python Projects on Github",
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
    offline.plot(fig, filename="python_repos.html")

if __name__ == '__main__':
    r = get_api_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_data(repo_dicts)
    make_visualization(repo_links, stars, labels)