import poker1
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    card=[]
    card = ['AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
            'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
            'AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
            'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']
    random.shuffle(card)
    pair1=[]
    pair2=[]

    for i in range(0,5):
        pair1.append(card[i])

    for i in range(5,10):
        pair2.append(card[i])
    output=""
    res=[]
    res=poker1.check(pair1,pair2)
    if res == pair1:
        output="USER WINS"
    else:
        output="COMPUTER WINS"
    return render_template('home.html', user1_card= pair1,user2_card=pair2,winner=output)

if __name__ == '__main__':
    print(app.config)
    app.config['DEBUG'] = True
    app.run()                 #by default runs on port 5000
                              # to launch WSIJ server
