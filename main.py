active = True
path = input("Enter a relative or absolute path of a text file containing questions:\n")

try:
    with open(path) as file:
        current_file = set()
        for question in  file:
            if question == "---\n":
                break
            else:
                current_file.add(question)

except FileNotFoundError:
    print(f"The path '{path}' doesn't match any file")
except IsADirectoryError:
    print(f"The path {path} is a folder, not a file")
else:
    for pair in current_file:
        question_answer = pair.split("** ") #Patter inside file might change
        if active:
            print("\n_______________________________________________________")
            print(question_answer[0])
            print("_______________________________________________________\n")
            while True:
                user_input = input(
                    "\n'Enter' for continuing\n'answer' for displaying answer\n'quit' for"
                    " quitting\n").lower()
                if not user_input or user_input == "enter":
                    break
                elif user_input == "q" or user_input == "quit":
                    active = False
                    break
                elif user_input == "answer":
                    try:
                        print("\n_______________________________________________________")
                        print(f"ANSWER: {question_answer[1]}")
                        print("_______________________________________________________\n")
                        break #if answer is shown, skip to the next one

                    except IndexError:
                        print("The file does not contain any answers")
                        print("_______________________________________________________\n")
                else:
                    print(f"That is not a valid option")
        else:
            break



