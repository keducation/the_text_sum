# TheTextSum

This project does exactly as its name suggests: takes a body of text and summarizes it.


An overview of the inner workings is as follows:
1) Import text from file
2) Clean-up data so it removes things such as special characters, stop words, punctuations, etc.
3) Create a list of word tokens and calculate each words' frequencies (how many times it has appeared in the text)
4) Tokenize the sentences in the imported text
5) Calculate the weighted frequency for each sentence based off of the word frequencies
6) Creation of summary by selecting the top 30% of weighted sentences
7) Export newly generated summary to a text file


The heavy lifters for this project are as follows:
- NLTK toolkit
- nalargest library


How to use this program:
- Simply change the variables for your text file name as well as the desired output file name and run the code
- There are comments in the code for easier identification
- The tested text files as well as their generated outputs are included for cross-testing


Demonstration video (click on the thumbnail to go to YouTube:
[![Click me to go to YouTube](https://img.youtube.com/vi/MH_vVYadtXY/0.jpg)](https://www.youtube.com/watch?v=MH_vVYadtXY)
