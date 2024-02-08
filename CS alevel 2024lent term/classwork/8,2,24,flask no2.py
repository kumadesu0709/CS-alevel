from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_next_birthday')    
def calc_next_birthday():
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
        return f'Your next birthday is {next_birthday}<br>You have {days_to_birthday} days until your next birthday<br>You will be {age} years old'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)