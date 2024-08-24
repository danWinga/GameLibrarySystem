from flask import Flask, jsonify , request# type: ignore
from flask_cors import CORS

app  = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r"/*":{'origins':'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})
 

 # hello  word route

@app.route('/', methods=['GET'])
def greetings():
    return ("Hello , world")

@app.route('/sharks', methods=['GET'])
def sharks():
    return ("Sharks!")

GAMES = [
    {
        "title": "2k21",
        "genre" : "sports",
        "played" :True,
    },
    {
        "title": "Evil Within",
        "genre" : "horror",
        "played" :False,
    },
    {
        "title": "the last  of us",
        "genre" : "survival",
        "played" :True,
    },{
        "title": "days gone",
        "genre" : "horror/survival",
        "played" :True,
    },
    {
        "title": "mario",
        "genre" : "retro",
        "played" :False,
    },
    
]

# The GET route handler
@app.route('/games', methods=['GET','POST'])
def all_games():
    response_object ={'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'title':post_data.get('title'),
            'genre':post_data.get('genre'),
            'played':post_data.get('played')
            })
        response_object['message'] = 'Game Added!'

    else:
        response_object['games'] =GAMES
    return jsonify(response_object)



if __name__ == "__main__":
    app.run(debug=True)