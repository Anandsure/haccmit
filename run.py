from flask import Flask, render_template,request
import json, requests
import quiz as q
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def paige():
   return render_template('index.html')

@app.route('/quiz/send',methods=['POST', 'GET'])
def main():
   if request.method == 'POST':
      resp_json = request.get_json()
      options = resp_json['deets']
      print(options)
      qns = q.get_quiz(options[0],options[1])
      print(json.dumps(qns,indent=4))
   return json.dumps({"response": 'could be anything noone cares'}), 200


   
if __name__ == '__main__':
   app.run(debug=True)
