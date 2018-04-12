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
   #getting health news from various news sources

    health_sources = get_sources('health')
    print(health_sources)
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('index.html',title = title,healthsource = health_sources)




