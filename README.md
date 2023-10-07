# Questio-Shuffler
Question Shuffler enhances the studying process by making it more active. It is a CLI python-based program, which takes a formatted .txt or .md file with question-answer pairs in it, and outputs the questions one by one waiting for the user to choose one of three different options.

## How does Questions Shuffler make learning more active?

### Creating Good Questions
The effectiveness of the program will be directly proportional to the quality of the questions the user create. So, by setting a subject or topic to study, the user has to investigate, gather,and analyze information about it. The better the information is digested or understood, the smarter the questions will be. Questions with short and specific answers are encouraged, it would turn the process more dynamic than having to answer a long answer, besides being harder to formulate such questions.

### Information Retrieval
Instead of looking at a cheat sheet with information, the dynamic of the questions presents the opportunity to pull information from the user's memory which is more active. The more the information is retrieved, the connections in the brain are stronger. This means that the access to said information would be faster and it is less likely to forget.

### Opportunity to make mistakes
While not answer is shown to the user, they have to work on retrieving the information required. In the case of not knowing the answer for whatever reason, the user can check the actual answer and rectify. The act of simply trying to come up with with an answer from the user's own words, even if is not complete nor using proper vocabulary, helps tremendously by increasing the participation and the intuitive idea that is being presented. 

## Options
- **Answer**: it displays to the present questions and skip to the next one
- **Enter**: will display for the next question 
- **Quit**: will end the program

## Format of Text File
*The question-answer pair must be on the same line for the program.*
The format for the file would be as follows:

```
**Question** Answer
**Question** Answer
**Question** Answer

---
 
Additional information
Additional information
Additional information
```

Whatever is after the 3 dashes will not be consider for the process of creating the questions, it only serves the purpose of having an additional space for notes. Neither the dashes nor the additional information are required, but recommended for future user reference. 

## How to use
Use the following command to get cloned the repository on Linux:

`git clone https://github.com/laotzee/Question-Shuffler.git`

The main file can be executed with a python interpreter. A sample file is provided to test the program itself. 

## Screenshots
![2023-10-07_16-16](https://github.com/laotzee/Question-Shuffler/assets/108775728/99996aa0-0377-4cd6-aba4-ae4dfe26102e)

## Contact
If you have any questions, feedback, or would like to get in touch, please feel free to do so via email at Gonzalezdeabreu@gmail.com

## Credits
The present project has been inspired by the book of Barbara Oakley "Learning like a Pro", specifically the passage where active learning and retrieval is discussed. The author not only provides a wide range of books on learning, but co-created the MOOC "Learning How to Learn: Powerful Mental Tools to Help You Master Tough Subjects". 

