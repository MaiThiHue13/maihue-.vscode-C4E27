from flask import Flask, render_template
from mlab import river
app = Flask(__name__)


# @app.route('/')
# def index():
    # return render_template('index.html')

@app.route('/all_river/<lengths>')
def all_river(lengths):
    rivers =  river.find({"continent":"S. America"})
    return render_template("river_length.html",all_river = rivers)

if __name__ == '__main__':
  app.run( debug=True)
 