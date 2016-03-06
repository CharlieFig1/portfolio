from flask import Flask, render_template, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import BaseQuery
import datetime
import requests, json
from math import ceil
from tapstream import refresh_token
from werkzeug.contrib.cache import SimpleCache

CACHE_TIMEOUT = 300

cache = SimpleCache()

class cached(object):

    def __init__(self, timeout=None):
        self.timeout = timeout or CACHE_TIMEOUT

    def __call__(self, f):
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator


app = Flask(__name__)

REFRESH_TOKEN = refresh_token()
ACCESS_TOKEN = 'yfmJXdWHe5FNqhRzqFjtdhhckKVNFI'
RESULTS_PER_PAGE = 10

def leaderboard(page):
    global ACCESS_TOKEN
    RESULTS_PER_PAGE = 10 * page
    str1 = "https://app.tapstream.com/api/v1/reports/rollup/?"
    str2 = "start_date=2015-01-01"
    str3 = "&dimensions=hit_param_value&metrics=converting_hit_count"
    str4 = "&filters=campaign_name|EXACT|Winter+Ambassadors+%282016%29"
    str5 = "&results=%i&order_by=-converting_hit_count" % (RESULTS_PER_PAGE)
    url = str1 + str2 + str3 + str4 + str5
    headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        ACCESS_TOKEN = REFRESH_TOKEN['access_token']
        headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,}
        r = requests.get(url, headers=headers)
    data = r.json()
    users = len(data)
    return data, users

def tapdata():
    str1 = "https://app.tapstream.com/api/v1/reports/rollup/?"
    str2 = "start_date=2015-01-01"
    str3 = "&dimensions=hit_param_value&metrics=converting_hit_count"
    str4 = "&filters=campaign_name|EXACT|Fall+Ambassadors+%282015%29"
    url = str1 + str2 + str3 + str4
    headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,}
    
    r = requests.get(url, headers=headers)
    data = r.json()
    return data

def tapSearch(username=None):
    results = []
    data = tapdata()

    if username != None:
        for result in data:
            if username.lower() in result['hit_param_value'].lower():
                results.append(result) 
    return results

@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>')
def index(page):
    data, users = leaderboard(page)
    return render_template('main.html', data=data,
                             users=users,
                             page=page)

@app.route('/search/', methods=['GET', 'POST'])
def search(page=1):
    if request.method == 'POST':
        username=request.form['search']
        if username == "":
            results = ""
        else:
            results = tapSearch(username)[0:10]
        
        users = len(results)

        return render_template('search.html', data=reversed(results),
                                 users=users, page=page,
                                 username=username)
    else:
        username = "" 
        results = "" 
        users = len(results)
        return render_template('search.html', data=reversed(results),
                                 users=users, page=page,
                                 username=username)

if __name__ == '__main__':
    app.run(debug=True)

