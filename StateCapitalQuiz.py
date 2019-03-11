import random

# Dictionary of the valid quizzes available to the user.
data_files = {"East": "states_east.txt",
              "West": "states_west.txt",
              "South": "states_south.txt",
              "Central": "states_central.txt",
              "All": "states_all.txt"
              }

# Loads the text file, one state/capital combination per line (separated by a tab character)
def read_states_into_dict(file_name):
    state_file = open(file_name, "r")
    d = {}

    for line in state_file:
        line_list = line.split("\t")
        d[line_list[0]] = line_list[1].strip()
    return d

# Implements a loop that will quiz the user until the user types "quit" or correctly answers all questions
def quiz(d):
    correct = 0
    guesses = 0
    states = list(d.keys())

    while len(states) != 0:
        state = random.choice(states)
        answer = input("What is the capital of " + state + "?")
        if answer == d[state]:
            states.remove(state)
            print("Correct!")
            guesses += 1
            correct += 1
        elif answer == "quit":
            break
        else:
            print("Incorrect! The capital is", d[state])
            guesses += 1

    print("You got", correct, "correct in", guesses, "guesses!")

# Asks the user to select the data file they want to use for the quiz and makes sure it is a valid selection.
def get_datafile_choice():
    regions = list(data_files.keys())
    choice = input("Choose a region: East, West, South, Central, or All.").title()
    while choice not in regions:
        choice = input("Invalid input.")
    return data_files[choice]


def main():
    file_name = get_datafile_choice()
    d = read_states_into_dict (file_name)
    quiz (d)


main()