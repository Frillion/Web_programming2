from bottle import *
from sys import argv
@route('/')
def index():
    info = {'home':'Home','info':{'Friðrik':'0908012440','Ari':'0605025169'},'Name':'Home'}
    return template('index.tpl',info)
@route('/<page>')
def KT(page):
    info = {'teacher':'Gunnar Þórunnarson','developer':'Friðrik Fannar Söebech','home': 'Home', 'info': {'Friðrik': '0908012440', 'Ari': '0605025169','Daníel':'2105012230'},'Name':'Home','Sum':'none'}
    if page == info['info']['Friðrik']:
        sum = 0
        for i in page:
                sum = sum+int(i)
        info['Sum'] = str(sum)
        info['Name'] = 'Friðrik'
    if page == info['info']['Ari']:
        sum = 0
        for i in page:
            sum = sum + int(i)
        info['Sum'] = str(sum)
        info['Name'] = 'Ari'
    if page == info['info']['Daníel']:
        sum = 0
        for i in page:
            sum = sum + int(i)
        info['Sum'] = str(sum)
        info['Name'] = 'Daníel'
    return template('index.tpl',info)
run(host='0.0.0.0', port=argv[1], reloader=True, debug=True)