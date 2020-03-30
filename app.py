from flask import Flask
from apis import blueprint as api
from waitress import serve

app = Flask(__name__)
app.register_blueprint(api,url_prefix='/api/v1')
app.config['BUNDLE_ERRORS'] = True
app.config['DEBUG'] = True
app.config["SWAGGER_UI_JSONEDITOR"]=True
# app.run(port=1234)
serve(app,port=1234)