from flask import Flask
from flask import request, render_template
import datetime

app = Flask(__name__)

@app.route('/')


@app.route('/getbday', methods = ["POST", "GET"])
def calc_next_birthday():
    if request.method == 'POST':
        birthday = request.form['birthday']
        dob = datetime.date.fromisoformat(birthday)
        today = datetime.date.today()
        birthday_this_year = datetime.date(today.year, dob.month, dob.day)
        birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)
        if birthday_this_year > today:
            next_birthday = birthday_this_year
        else:
            next_birthday = birthday_next_year
        days_to_birthday = (next_birthday - today).days
        age = (next_birthday - dob).days // 365
        return render_template('updated_bday.html',dob = dob, next_birthday = next_birthday, days_to_birthday = days_to_birthday, age = age, today = today)
    else:
        birthday = " "
        return render_template('updated_bday.html',dob = '', next_birthday = '', days_to_birthday = '', age = '', today = '')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

"""@app.route('/getname', methods = ["POST", "GET"])
def get_name():
    if request.method == 'POST':
        typed_name = request.form['name']
    else:
        typed_name = ''
    return render_template('greet_form.html', name = typed_name)"""
