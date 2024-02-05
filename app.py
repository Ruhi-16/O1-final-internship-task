
from flask import Flask, render_template, session
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Change this to a secure random key in production

@app.route('/url/task')
def task_page():
    # Increment visit count
    session['visit_count'] = session.get('visit_count', 0) + 1

    # Generate a random number
    random_number = randint(1, 100)

    return render_template('task.html', visit_count=session['visit_count'], random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
