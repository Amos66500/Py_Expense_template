from PyInquirer import prompt
import csv

user_questions = [
        {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    # Here we create a row from the dictionnary 'infos' to get the value from each key
    row_infos = []
    for key, value in infos.items():
        row_infos.append(value)
    
    # Here we open the csv file in append mode and we add a row with the row_infos data
    with open('users.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row_infos)

    print("User Added !")
    return True