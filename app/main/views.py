from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Newsarticle,Newssources


#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
   #getting news from various news sources

    health_sources = get_sources('health')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    general_sources = get_sources('general')
    science_sources = get_sources('science')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('index.html',title = title,healthsource = health_sources,biznews = business_sources,general = general_sources,enta = entertainment_sources,sports = sports_sources,science = science_sources,tech = technology_sources)




@main.route('/BusinessSources/')
def BusinessSources():
    '''
    view root page function that returns  business news from various news sources
    '''
   

    
    business_sources = get_sources('business')
   
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('biz.html',title = title,biznews = business_sources)