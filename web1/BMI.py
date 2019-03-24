# Anh xem cho e bài này với bài username, nó không ra  :(((, e tìm mãi mà chẳng biết sai ở đâu:((((((((

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/BMI/<int:weight>/<int:height>')
def BMI(weight, height):
    height = height/100
    BMI = weight/(height*height)
    if BMI<16:
        BMI = "BMI: + 'str(BMI)'+ Severely under weight"
    elif BMI<18.5:
        BMI = "BMI: + 'str(BMI)'+ Under weight"
    elif BMI<25:
        BMI = "BMI: +'str(BMI)'+ Normal"
    elif BMI<30:
        BMI = "BMI: +'str(BMI)'+ Overweight"
    else:
        BMI = "BMI: +'str(BMI)'+ Obese"
    
    return  render_template('BMI.html', BMI = BMI)
if __name__ == '__main__':
  app.run(debug=True)
 