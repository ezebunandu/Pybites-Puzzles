import glob
import json
from urllib.parse import urljoin
from urllib.request import urlretrieve
import re

BASE_URL = "http://projects.bobbelderbos.com/pcc/omdb/"
MOVIES = ("bladerunner2049 fightclub glengary " "horrible-bosses terminator").split()
TMP = "..tmp"

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f"{movie}.json"
    remote = urljoin(BASE_URL, fname)
    local = urljoin(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(urljoin(TMP, "*json"))


def get_movie_data(files=files):
    """Returns a list of dict for each json file in files"""
    movie_data = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            movie_data.append(dict(data))
    return movie_data


def get_single_comedy(movies=get_movie_data()):
    comedies = [movie["Title"] for movie in movies if "Comedy" in movie["Genre"]]
    return comedies[0]


def get_movie_most_nominations(movies=get_movie_data()):
    """Returns the movie with the most nominations"""
    PATTERN = r"& (\d+) nominations"
    nominations = {
        movie["Title"]: int(re.findall(PATTERN, movie["Awards"])[0]) for movie in movies
    }
    nominations = sorted(nominations.items(), key=lambda kv: kv[1], reverse=True)
    return nominations[0][0]


def get_movie_longest_runtime(movies=get_movie_data()):
    PATTERN = r"(\d+) min"
    runtimes = {
        movie["Title"]: int(re.findall(PATTERN, movie["Runtime"])[0])
        for movie in movies
    }
    runtimes = sorted(runtimes.items(), key=lambda kv: kv[1], reverse=True)
    return runtimes[0][0]
