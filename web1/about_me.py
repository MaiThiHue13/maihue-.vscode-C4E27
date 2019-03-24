from flask import Flask,render_template
app = Flask(__name__)
import os
from flask import Flask, redirect, url_for


#ex1
@app.route('/')
def index():
  return ("hello Huế")


@app.route('/about_me')
def about_me():
    about_me = {
      "name":" Hue",
      "work":" SV",
      "school":" VCU",
      "hobbie":" Vẽ"
    }

    return render_template('about_me.html', about_me = about_me)


@app.route('/school')
def school():
  return redirect ("http://techkids.vn")

if __name__ == '__main__':
  # port = int(os.environ.get('PORT', 5000))
  app.run( debug=True)
 
