from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def play_rps():
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(user_choice, computer_choice)
        return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html')

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == '__main__':
    app.run(debug=True)