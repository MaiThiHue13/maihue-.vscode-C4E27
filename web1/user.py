from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def users(username):
    users = {
        "hue":{
            "name":"Huế",
            "gender":"nữ",
            "age":"20",
            "hobbie":"vẽ"
        },
        "duyen":{
            "name":"Duyên",
            "gender":"nữ",
            "age":25,
            "hobbie":"ngủ"
        },
        "hien":{
            "name":"Hiền",
            "gender":"nữ",
            "age":45,
            "hobbie":"trồng hoa"
        }
    }
    if username in users:
        user = users[username]
        return render_template('user.html', user = user)
    else:
        return 'User not found'


if __name__ == '__main__':
  app.run(debug=True)
 