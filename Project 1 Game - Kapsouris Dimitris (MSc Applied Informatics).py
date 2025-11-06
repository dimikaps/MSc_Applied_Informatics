from random import sample  # Sample function gives us as many options as are declared in the parameter (line 19, 2nd parameter)


game_data = {  # Here i used a dictionary to store all the questions along with their answers. I could use a list or another data structure but i decided that dictionary fits better.
    "An algorithm is a sequence of steps that leads to solving a problem." : True,
    "The CPU is responsible only for storing data.": False,
    "RAM is volatile memory, meaning it loses its data when the computer is turned off.": True,
    "The operating system is software that manages hardware and software resources.": True,
    "Python is a low-level programming language.": False,
    "Bits and bytes are used to measure CPU processing speed.": False,
    "The HTTP protocol is used to transfer web pages over the Internet.": True,
    "The BIOS is software that runs before the operating system loads.": True,
    "Cloud computing allows data to be stored and processed only locally on the computer.": False,
    "Databases are used to store and retrieve information in an organized way.": True
}

correct_answers = 0
wrong_answers = 0
chosen_questions = sample(list(game_data.keys()), 5)
for question in chosen_questions:
    print(question)
    while True:
        user_answer = input("What is the right answer (Type T for True or F for False): ").upper().strip()  # I used the upper() method to modify the user input to uppercase and strip() to removes spaces
        if user_answer == 'T':  # At this point I convert the user_answer from str to boolean
            user_answer = True
            break
        elif user_answer == 'F':
            user_answer = False
            break
        else:
            print("Invalid answer, try again")
    
    if game_data[question] == user_answer:  # Here we check the answer of the user, with the correct answer
        correct_answers += 1
        print(f"Your answer to the question is {user_answer} and you are right!")
    else:
        wrong_answers += 1
        print(f"Your answer to the question is {user_answer} and you are wrong!")

score = 100 * (correct_answers / 5)
print(f"You had {correct_answers} correct answers and {wrong_answers} wrong answers, and your score is {score}\nGame Over")


'''
Create a quiz game where the program randomly asks the player a series of questions.
The total number of questions available (the “question bank”) is 10.

The player will be asked 5 questions, randomly selected from the 10.
Each time a question appears, the user must type an answer using the keyboard.
The program will immediately display the result of the answer with the messages "CORRECT" or "WRONG".

At the end, the program should display the player's final score, showing:

how many correct and incorrect answers they gave, and

the percentage of correct answers, calculated as:
100 * (number_of_correct_answers / 5)

'''
