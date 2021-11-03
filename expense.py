from PyInquirer import prompt
import csv


# Function who open the users.csv file and give a list of users for the spender question
def get_users():
    options = []
    with open('users.csv', newline='') as users_csv_file:
        reader = csv.reader(users_csv_file, delimiter=' ')
        for row in reader:
            options.append(row[0])
    return options

def involved_people(answers):
    options = []
    for users in get_users():
        if users != answers['spender']:
            options.append({'name': users, 'checked': False})
    return options

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_users(),
    },
    {
        "type":"checkbox",
        "name":"involved_people",
        "message":"New Expense - Involved People: ",
        "choices": involved_people,
    },
]


def new_expense(*args):
    infos = prompt(expense_questions)
    # Here we create a row from the dictionnary 'infos' to get the value from each key
    row_infos = []
    for key, value in infos.items():
        row_infos.append(value)

    # Here we open the csv file in append mode and we add a row with the row_infos data
    with open('expense_report.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row_infos)

    print("Expense Added !")
    return True


