
def print_item(message):
    """Prints a formatted message with two horizontal lines"""
    print("\n_______________________________________________________")
    print(message)
    print("_______________________________________________________\n")

def question_pair(file):
    """Returns a set with questions, file format required. Exception raises if
    no file is provided"""
    current_file = set()
    if file and isinstance(file, str):
        for question in  file:
            if question == "---\n":
                break
            else:
                current_file.add(question)
        return current_file
    else:
        raise FileError("Not proper file was not provided")

user_message = ("\n'Enter' for continuing\n'answer' for displaying answer\n "
    "'quit' for exitting\n")

active = True
path = input("Enter a relative or absolute path of a text file containing "
             " questions:\n")
try:
    with open(path) as file:
        current_file = question_pair(file)
        break

except FileNotFoundError:
    print(f"The path '{path}' doesn't match any file")
    exit()

except IsADirectoryError:
    print(f"The path {path} is a folder, not a file")
    exit()

except:
    print("Something went wrong")
    exit()

for pair in current_file:
    if active:
        question_answer = pair.split("** ") #Patter inside file might change
        print_item(question_answer[0])
        while True:
            user_input = input(user_message).lower()
            if not user_input or user_input == "enter":
                break
            elif user_input == "q" or user_input == "quit":
                active = False
                break
            elif user_input == "answer":
                try:
                    print_item(question_answer[1])
                    break #if answer is shown, skip to the next one

                except IndexError:
                    print_item("The file does not contain any answers")
            else:
                print(f"That is not a valid option")
    else:
        break



