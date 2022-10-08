
from secrets import choice
#import random


ques=[
    'Who is the developer of Python language',
     'When did India get independence',
     'What is the currency of India?',
     'Which state does Bangalore belogs to?',
     'How many members in BTS (Bangtan boys)?'
]

ans=[
    'Guido Van',
    '1947',
    'INR',
    'Karnataka',
    '7'
]

option=[
    ['Dennis Ritchi','Alan Frank','Guido Van','Albert'],
    ['1957','1956','1947','1900'],
    ['Pounds','Euros','Dollars','INR'],
    ['Karnataka','Andhra','Tamilnadu','Kerala'],
    ['6','7','8','5'],
]

def play_game(name, ques, ans, option):   #to recieve the name in the func name is written as a parameter
    print(f"Hello {name.title()} to the KBC game")     #string formating
    #print("Hello",name,"to the KBC game")
    score = 0
    
    for i in range(len(ques)):
        
        current_ques = ques[i]
        #current_ques = random.choice(ques)
        correct_ans = ans[i]
        current_ques_option = option[i] 
        print("Question : ",current_ques)
        for index, each_option in enumerate(current_ques_option) :  
            print(index+1, ")",each_option)
        user_ans_index = int(input("Enter your choice (1,2,3 or 4) :"))
        user_ans = current_ques_option[user_ans_index-1]
        if user_ans == correct_ans :
            print("Correct Answer")
            score = score + 100
        else:
            print("Wrong Answer")
            break


    print("Your final score is :", score)
    return name, score

def view_score(name_n_score):
    for name, score in name_n_score.items():
        print(name, "has scored",score)

def game(ques, ans, option):
    name_n_score = {}
    while True:
        print("Welcome to the KBC game")
        print("1) Play Game\n2) View Scores\n3) Exit")
        choice = int(input("Please enter ur choice:"))
        if choice==1:
            name= input("please enter ur name:")         #to pass the name in the func name is written as a parameter
            name, score =  play_game(name, ques, ans, option)          
            name_n_score[name] = score
        
        elif choice==2:
            view_score(name_n_score)
        elif choice==3:
            break
        else:
            print("Your choice is not valid")
        

game(ques, ans, option)  
