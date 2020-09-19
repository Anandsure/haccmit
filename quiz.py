import requests
import json

def get_quiz(cat,ty):
    topics = {'GK':9,'Entertainment':11,'video_games':15,'nature':17,'computers':18,'math':19,'sports':21,'history':23,'politics':24,'gadgets':30,'anime':31} #we'll get this from form
    type_o_qn = {'True_or_False':'boolean','MCQ':'multiple'}

    x = requests.get('https://opentdb.com/api.php?amount=5&category='+str(topics[cat])+'&difficulty=easy&type='+type_o_qn[ty])
    return x.json()

if __name__ == '__main__':
    y = get_quiz("GK","True_or_False")
    print(json.dumps(y,indent=4))


