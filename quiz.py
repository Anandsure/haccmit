import requests
import json

#defining the post vars here broo :3

amount = 5
topics = {'GK':9,'Entertainment':11,'video games':15,'nature':17,'computers':18,'math':19,'sports':21,'history':23,'politics':24,'gadgets':30,'anime':31} #we'll get this from form
#difficulty can be kept as easy 
type_o_qn = {'True_or_False':'boolean','MCQ':'multiple'}

x = requests.get('https://opentdb.com/api.php?amount=5&category='+str(topics['sports'])+'&difficulty=easy&type='+type_o_qn['MCQ'])
print(json.dumps(x.json(), indent=4))

#the json looks like this :

'''
{
    "response_code": 0,
    "results": [
        {
            "category": "Sports",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Which driver has been the Formula 1 world champion for a record 7 times?",
            "correct_answer": "Michael Schumacher",
            "incorrect_answers": [
                "Ayrton Senna",
                "Fernando Alonso",
                "Jim Clark"
            ]
        },
        {
            "category": "Sports",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What was the final score of the Germany vs. Brazil 2014 FIFA World Cup match?",
            "correct_answer": "7 - 1",
            "incorrect_answers": [
                "0 - 1",
                "3 - 4",
                "16 - 0"
            ]
        },
        {
            "category": "Sports",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What is the most common type of pitch thrown by pitchers in baseball?",
            "correct_answer": "Fastball",
            "incorrect_answers": [
                "Slowball",
                "Screwball",
                "Palmball"
            ]
        },
        {
            "category": "Sports",
            "type": "multiple",
            "difficulty": "easy",
            "question": "&quot;Stadium of Light&quot; is the home stadium for which soccer team?",
            "correct_answer": "Sunderland FC",
            "incorrect_answers": [
                "Barcelona FC",
                "Paris Saints-Germain",
                "Manchester United"
            ]
        },
        {
            "category": "Sports",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Which year did Jenson Button won his first ever Formula One World Drivers&#039; Championship?",
            "correct_answer": "2009",
            "incorrect_answers": [
                "2010",
                "2007",
                "2006"
            ]
        }
    ]
}
'''

