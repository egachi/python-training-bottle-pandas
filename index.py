
import bottle
from bottle import route, run, Response, template
import json
import pandas as pd
import os
from ftfy import fix_text
from pathlib import Path

f = "resources/data.csv"
data={}
results={}

def savingToJson(filename, results):
    file = Path(filename)
    file.touch(exist_ok=True)
    filehandle =open(filename, "a+")
    filehandle.writelines(results)
    filehandle.seek(0)
    filehandle.close()

@route('/')
def index():
    """Home page"""
    results = getstations(114897)
    savingToJson("trained_data.json", results)
    fixed_text = fix_text(results)
    data = json.loads(fixed_text)
    title="STATIONS"
    return template('index.tpl',data=data, title=title)

@route('/api/stations/<id:int>')
def getstations(id):
    n = id
    dataset = pd.read_csv(f)
    results = dataset.loc[1:id, ['STATION','NAME']].to_json(orient='records')
    return json.dumps(results)
	
if __name__ == '__main__':
	run(host='0.0.0.0', port=8000, debug=True, reloader=True)
	
app_server = bottle.default_app()
