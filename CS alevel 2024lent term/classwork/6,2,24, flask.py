from flask import Flask
from flask import request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return f'Hello anonymous person.'

@app.route('/hello/')
@app.route('/hello/<name>')
def greet(name=''):
    return render_template('hello.html',name=name)

@app.route('/add')
def add():
    first_number = request.args.get('first','')
    second_number = request.args.get('second','')
    if first_number and second_number:
        try:
            result = int(first_number) + int(second_number)
        except ValueError:
            return 'invalid data'
        return f'{first_number} + {second_number} = {result}'
    else:
        return 'No arguments detected'

@app.route('/calculate_next_birthday')    
def calc_next_birthday(year_of_birth='',month_of_birth='',day_of_birth=''):
    year_of_birth = int(request.args.get('year', ''))
    month_of_birth = int(request.args.get('month', ''))
    day_of_birth = int(request.args.get('day',''))
    if day_of_birth and month_of_birth and year_of_birth:
        try:
            dob = datetime.date(year_of_birth,month_of_birth,day_of_birth)
            today = datetime.date.today()
            birthday_this_year = datetime.date(today.year, dob.month, dob.day)
            birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)
            if birthday_this_year > today:
                next_birthday = birthday_this_year
            else:
                next_birthday = birthday_next_year
            days_to_birthday = (next_birthday - today).days
            age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
        except ValueError:
            return 'invalid data'
        return render_template('birthday.html',dob = dob, next_birthday = next_birthday, days_to_birthday = days_to_birthday, age = age, today = today)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)