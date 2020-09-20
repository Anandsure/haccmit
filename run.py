from flask import Flask, render_template,request
import json, requests
import quiz as q
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def paige():
   return render_template('index.html')

@app.route('/quiz')
def qnss():
   return render_template('qns.html', all_qns = aq , all_ans = ica)

@app.route('/quiz/send',methods=['POST', 'GET'])
def main():
   if request.method == 'POST':
      resp_json = request.get_json()
      options = resp_json['deets']
      qns = q.get_quiz(options[0],options[1])
      # print(json.dumps(qns,indent=4))
      global aq
      aq = []
      global ica
      ica = []
      check = {}
      for i in range(5):
         check.update({qns["results"][i]["question"]:qns["results"][i]["correct_answer"]})     
      for i in range(5):
         aq.append(qns["results"][i]["question"])
         interim = list(qns["results"][i]["incorrect_answers"])
         interim.append(qns["results"][i]["correct_answer"])
         ica.append(interim)
      print(ica)
      
   # return render_template('qns.html', all_qns = aq , all_ans = ica)

   return json.dumps({"response": 'could be anything noone cares'}), 200


   
if __name__ == '__main__':
   app.run(debug=True)
