from flask import Flask, render_template, request
from googleapiclient.discovery import build

import api
import emotion

app = Flask(__name__)

# YouTube API key
API_KEY = "AIzaSyAI_pp6cVpDKzJqkWzlldgU94I_cgvPCYM"


@app.route('/')
def index():
    return render_template('indexx.html', result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    #for video_id
    video_id = request.form['video_id']
    result = 0


    f = api.create_comments(video_id)

    e = emotion.strat_emotion_eng(f)

   

    if(e == 1):
        return render_template('result.html')
        # return render_template('indexx.html', result=1)
    else:
        return render_template("failed.html")
        # return render_template('indexx.html', result=0)
    

if __name__ == '__main__':
    app.run(debug=True)

