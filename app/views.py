from flask import render_template
from app import app
from .request import get_sources,get_source,get_articles


@app.route('/')
def index():
  '''
  View source page function that returns the source details page and its data
  '''
  business_sources = get_sources('business')
  technology_sources = get_sources('technology')
  sports_sources = get_sources('sports')
  title = 'Home - Welcome to The best Source Review Website Online'
  return render_template('index.html', title = title, business = business_sources, technology = technology_sources, sports =  sports_sources )

@app.route('/article/<source_name>')
def article(source_name):
  '''
  View article page function that returns the article details page and its data
  '''
  article = get_articles(source_name)
  title = f'{source_name}'

  return render_template('source.html',title = title,articles = article)
  
   