from flask import render_template
from app import app
# from .request import get_sources
from .request import get_sources,get_source

@app.route('/')
def index():

    '''
    View source page function that returns the source details page and its data
    '''
   #  source = get_source(name)
   #  title = f'{source.title}'
  # Getting popular source
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    title = 'Home - Welcome to The best Source Review Website Online'
    return render_template('index.html', title = title, business = business_sources, technology = technology_sources, sports =  sports_sources )