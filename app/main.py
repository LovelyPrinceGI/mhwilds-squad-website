from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="../templates", static_folder="../static")

#--------------------------------------------------
# Try making static routes
#--------------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    hunter_specification = ['Any HR welcome!', 'Beginner welcome!', 'Professional/ Expert welcome!']
    return render_template("about.html", myhunter_specification = hunter_specification)

@app.route('/squad')
def squad_name():
    data = {
        "name": ["Blaze"],
        "main_weapon": ["Greatsword"],
        "role": ["Leader"]
    }
    df = pd.DataFrame(data)
    mydata = df.to_dict(orient='records')  # แปลงให้พร้อมใช้ใน HTML
    return render_template("squad.html", mydata=mydata)



#------------------------------------------------
# Try making dynamic routes
#------------------------------------------------
@app.route('/user')
def user():
    # Name, Main Weapon, Role
    username = "Blaze"
    name = "Blaze"
    main_weapon = "Greatsword"
    role = "Leader"
    return render_template("user.html", username = username, myname = name, mymain_weapon = main_weapon, myrole = role)


if __name__ == "__main__":
    app.run(debug=True)