# Qffle
Qffle enhances studying by making it more active. It is a GUI Python-based program that takes a CSV file with question-answer columns. The user is presented with the question side of the card first and prompted to answer either right or wrong, depending on whether the user can recall the answer. The answer side is available at any moment for reference. Wrongly guessed cards will go into the deck again. Once all cards are finished, the program returns a report of the session time and right and wrong answers. 

## How does Qffle make learning more active?

### Creating Good Questions
The program's effectiveness will be directly proportional to the quality of the questions the user creates. By setting a subject or topic to study, the user has to investigate, gather and analyze information, and create the questions. The better the information is digested or understood, the smarter the questions will be. Questions with short and specific answers are encouraged, it would make the process more dynamic than having to answer a long answer, besides being harder to formulate such questions.

### Information Retrieval
Instead of looking at a cheat sheet with information, the dynamic of the questions presents the opportunity to pull information from the user's memory which is more active. The more information is retrieved, the more connections in the brain are stronger. This means that access to said information would be faster and it is less likely to be forgotten.

### Opportunity to make mistakes
Fliping the card inmediately is discouraged. The act of simply trying to come up with an answer from the user's own words, even if is not complete nor using proper vocabulary, helps tremendously by increasing the participation and the intuitive idea that is being presented. So, try to come up with an answer and check the card later.

## Format of CSV File
The first line would be taken as the headings for the cards, while the rest of the entries would be treated as the cards themselves.

```
Question heading, Answer heading
Question, Answer
Question, Answer
Question, Answer
Question, Answer
Question, Answer
Question, Answer
Question, Answer
```

There is a max and recommended amount of characters for the headings and the body of the cards to avoid going over the borders.

|         |Recommended|Max|
|---------|----------------|---------------|
|Headings| 10 characters|15 characters|
|Body| 100 characters|120 characters|

## How to use
Use the following command to clone the repository

`git clone https://github.com/laotzee/Question-Shuffler.git`

You can run the main.py with a Python3 interpreter.

A .exe and an .AppImage are available under the folder "executables"

## Screenshots
![questionDemo](https://github.com/user-attachments/assets/759c2a58-1bd6-4712-8a9d-b5cbd319150a)

![answerDemo](https://github.com/user-attachments/assets/f0b2d6fb-e18e-43b1-87d6-d0f3457be343)

![germanDemo](https://github.com/user-attachments/assets/49635b96-e587-4389-a4ac-2856222b7891)

![englishDemo](https://github.com/user-attachments/assets/95cd9af0-d848-4d59-8e22-8427d4c02080)

## Resources

By default, the program will only take 30 questions from a given file. Such a number can be changed inside the cards.py file by altering the constant READ_MAX.

Inside the resource folder, there are two files as demos. 

- test.csv: dummy file for displaying the max amount of characters
- most_used_german_words.csv: contains the 50000 most used German words and their English translation. Despite not being implemented yet, there is a column for counting the frequency of the user's correct answer and the frequency of the German words themselves.

## Contact
If you have any questions, or feedback, or would like to get in touch, please feel free to do so via email at contact@laotze.net

## Credits
The present project has been inspired by the book of Barbara Oakley "Learning Like a Pro", specifically the passage where active learning and retrieval is discussed. The author not only provides a wide range of books on learning, but co-created the MOOC "Learning How to Learn: Powerful Mental Tools to Help You Master Tough Subjects". 

