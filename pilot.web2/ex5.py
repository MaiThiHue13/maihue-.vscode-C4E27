from flask import Flask, render_template
from mlab import river
app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template('homepage.html')

@app.route('/all_river')
def all_river():
   rivers =  river.find()
   return render_template("river.html", all_river = rivers)

if __name__ == '__main__':
  app.run(debug=True)
 