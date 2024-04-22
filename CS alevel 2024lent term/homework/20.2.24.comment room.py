from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/comment', methods = ["POST", "GET"])
def comment():
    if request.method == 'POST':
        comments = []
        comment = request.form['comment']
        file = open('comments.txt', 'a')
        file.write(f"{comment}\n")
        file.close()
        with open('comments.txt', "r") as file:
            for line in file:
                comments.append(line) 
        return render_template('comment_room.html', comments = comments)
    else:
        comments = []
        return render_template('comment_room.html', comments = comments)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)