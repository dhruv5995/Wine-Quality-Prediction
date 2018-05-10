"""`main` is the top level module for your Flask application."""

# Imports
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Import the Flask Framework
from flask import Flask, request
app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')

    # render the web page with the data 
    return template.render()

    
@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    return template.render()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        result=request.form
        # import pdb; pdb.set_trace()
        val1 = float(result['var1'])
        val2 = float(result['var2'])
        val3 = float(result['var3'])
        val4 = float(result['var4'])
        val5 = float(result['var5'])
        val6 = float(result['var6'])
        val7 = float(result['var7'])
        val8 = float(result['var8'])
        val9 = float(result['var9'])
        val10 = float(result['var10'])
        val11 = float(result['var11'])
        val12 = float(result['var12'])

        inp = np.array([])
        inp = np.append(inp, [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]).reshape(-1,1)

        with open("model_rcf.pkl", "rb") as f:
            model = pickle.load(f)

        pred = model.predict(inp)

        if pred == 0:
            prediction = "It's bad wine"
        else:
            prediction = "It's good wine"

        return render_template('home.html', prediction = prediction)
