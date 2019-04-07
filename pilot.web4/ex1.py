from flask import *
from bike import bike_collection
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/new_bike', methods = ["GET","POST"])
def new_bike():   
  if request.method == "GET":
    return render_template("bike.html")
  elif request.method == "POST":
    form = request.form
    print(form)

    bike_model = form["input_model"]
    bike_daily_fee = form["input_daily_fee"]
    bike_image = form["input_image"]
    bike_year = form["input_year"]

    new_bike ={
      
      "model" : bike_model,
      "daily_fee" : bike_daily_fee,
      "image" : bike_image,
      "year" : bike_year
    }

    bike_collection.insert_one(new_bike)
    return "SUBMIT"

if __name__ == '__main__':
  app.run(debug=True)
 