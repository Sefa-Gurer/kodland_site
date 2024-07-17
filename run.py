from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'kodland'

def calculate_score(answers):
    score = 0
    correct_answers = {
        'question1': 'b',
        'question2': 'c',
        'question3': 'a',
        'question4': 'c',
        'question5': 'c',
        'question6': 'a',
        'question7': 'd',
        'question8': 'b',
        'question9': 'a',
        'question10': 'd'
    }
    for key, value in correct_answers.items():
        if answers.get(key) == value:
            score += 1
    return score * 10

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answers = {
            'question1': request.form.get('question1'),
            'question2': request.form.get('question2'),
            'question3': request.form.get('question3'),
            'question4': request.form.get('question4'),
            'question5': request.form.get('question5'),
            'question6': request.form.get('question6'),
            'question7': request.form.get('question7'),
            'question8': request.form.get('question8'),
            'question9': request.form.get('question9'),
            'question10': request.form.get('question10')
        }
        score = calculate_score(answers)
        session['current_score'] = score
        if 'best_score' not in session or score > session['best_score']:
            session['best_score'] = score
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    current_score = session.get('current_score', 0)
    best_score = session.get('best_score', 0)
    return render_template('result.html', current_score=current_score, best_score=best_score)

if __name__ == '__main__':
    app.run()
