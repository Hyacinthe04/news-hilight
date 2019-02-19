from app import app
import urllib.request,json
from .models import source
from .models import article

Source=source.Source
Article =article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCE_API_BASE_URL"]

# Getting the article base url
base_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)
    return source_results
def get_articles(author):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(author,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)
    return article_results


def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
       

        if name:
            source_object = Source(name,description,url,category)
            source_results.append(source_object)


    return source_results
def process_articles(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
       

        if name:
            article_object = Article(name,description,url,category)
            article_results.append(article_object)


    return article_results


def get_source(name):
    get_source_details_url = base_url.format(name,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            

            source_object = Source(name,description,url,category)

    return source_object
def get_article(author):
    get_article_details_url = base_url.format(name,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            author = article_details_response.get('author')
            title = article_details_response.get('title')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            

            article_object = Article(author,title,description,url,urlToImage)

    return article_object
