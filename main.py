from requests import get
import flask

app = flask.Flask(__name__)

def get_data(user):
    return(get('https://api.github.com/users/{}'.format(user)).json())

@app.route('/', methods=['GET'])
def main():
    return(flask.render_template('index.html'))

@app.route('/<user>', methods=['GET'])
def search(user):
    return(flask.render_template('search.jinja', data=get_data(user)))