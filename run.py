import os
import csv
import operator
from flask import Flask, render_template, redirect, request, session, url_for, flash
import quizdata


app = Flask(__name__)
app.secret_key = 'random string'

number_of_questions = 15
global username
global user_score


"""----- Functions -----"""


def write_to_file(filename, data):
    """ Handles the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)


def update_leaderboard(user_score, username):
    """ Adds username and score details into a csv file """
    with open('data/scores.csv', 'a') as f:
        fieldnames = ['Username', 'Score']
        update = csv.DictWriter(f, fieldnames=fieldnames)
        update.writerow({'Username' : username, 'Score' : user_score})


def getThingToSortBy(row):
    """ Turns user scores into integers for correct ordering """
    return int(row[0])


def sort_scores():
    """ Sorts user scores in order from highest to lowest """
    sample = open('data/scores.csv', 'r')
    reader = csv.reader(sample,delimiter=',')
    sort = sorted(reader,key=getThingToSortBy, reverse=True)
    return(sort)


"""----- Routes -----"""


@app.route('/', methods=["GET", "POST"])
def index():
    """ Asks the user to enter a username """
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['logged_in'] = True
        username = request.form["username"]
        return redirect(url_for('quiz'))
    if 'username' in session:
        username = session['username']
        return redirect(url_for('quiz'))
    return render_template("index.html", page_title="Unwanted Premier League records")


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    """ Runs through the quiz questions while keeping score """
    username = session['username']
    
    i = session.get('question_number')
    if i == None:
        i = 1
        session['question_number'] = i
        
    o = session.get('user_score')
    if o == None:
        o = 0
        session['user_score'] = o
    
    if request.method == 'GET':
        question = quizdata.question_prompts[i]["prompt"]
        options = quizdata.question_prompts[i]["options"]
        question_options = ', '.join(map(str, options))
        
    if request.method == 'POST':
        session['guess'] = request.form['guess'].strip(' \t\n\r').lower()
        guess = request.form["guess"].strip(' \t\n\r').lower()
        correct_answer = quizdata.question_prompts[i]["answer"].strip(' \t\n\r').lower()
        if guess == correct_answer:
            session['user_score'] = o + 3
            return redirect(url_for('reveal'))
        else:
            return redirect(url_for('reveal'))
    
    return render_template("quiz.html", page_title="Let's begin", display_question=question, display_options=options)


@app.route('/reveal', methods=["GET", "POST"])
def reveal():
    """ Reveals whether the user answered correctly and returns them to the next question """
    i = session.get('question_number')
    
    if i == None:
        i = 1
        session['question_number'] = i
    
    if request.method == 'GET':
        guess = session['guess']
        i = session['question_number']
        correct_answer = quizdata.question_prompts[i]["answer"].lower()
        if guess == correct_answer:
            reveal = "Correct! " + quizdata.question_prompts[i]["reveal"]
        else:
            reveal = "Unlucky. " + quizdata.question_prompts[i]["reveal"]
    
    if request.method == "POST":
        if session['question_number'] == number_of_questions:
            return redirect(url_for('endquiz'))
        else:
            session['question_number'] = i + 1
            return redirect(url_for('quiz'))
    
    return render_template("reveal.html", display_answer=correct_answer, display_reveal=reveal)


@app.route('/exit')
def exit():
   """ Removes the user from the session """
   session.pop('username', None)
   session['logged_in'] = False
   return redirect(url_for('index'))


@app.route('/endquiz', methods=["GET", "POST"])
def endquiz():
    """ Informs the user of their score at the end of the quiz """
    username = session['username']
    user_score = session['user_score']
    
    if user_score >= 36:
        display_score = "Congratulations! With {0} points you probably would have just about secured Premier League survival. Check out our leaderboard to see where you rank.".format(user_score)
    elif user_score < 11:
        display_score = "Oh dear. {0} points would have eclipsed the record for the worst ever Premier League points tally. Take a look to see if you fare any better on our leaderboard.".format(user_score)
    elif user_score < 25:
        display_score = "{0} points means guaranteed relegation and a season to forget. Take a look to see if you fare any better on our leaderboard.".format(user_score)
    else:
        display_score = "Not bad. It's unlikely that {0} would save you from relegation, but you've avoided setting any unwanted records. Check out our leaderboard to see where you rank.".format(user_score)
    
    if request.method == 'POST':
        update_leaderboard(username, user_score)
        
        """ Resets score and question number count before page is exited """
        i = session.get('question_number')
        if i >= 1:
            i = None
        session['question_number'] = i
    
        o = session.get('user_score')
        if o >= 0:
            o = None
        session['user_score'] = o
        return redirect(url_for('leaderboard'))
    
    return render_template("endquiz.html", display_score=display_score)


@app.route('/leaderboard')
def leaderboard():
    """ Ranks all user scores from highest to lowest """
    userscores = sort_scores()
    return render_template("leaderboard.html", page_title="Leaderboard", userscores=userscores)

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)