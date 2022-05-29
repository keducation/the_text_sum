import os, time
import nltk

from os import path
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from heapq import nlargest

text_name = "Book - Pride and Prejudice.txt"                                            # Change these variables to match your input data
output_name = "Book Summary.txt"

os.system("cls" if os.name == "nt" else "clear")                                        # Initialize stopwords and punctuation
print(f"Downloading stopword data and initializing punctuation data...\n")
nltk.download("stopwords")
stop_words = stopwords.words('english')
punctuation = punctuation + '\n'

project_path = path.dirname(__file__) if "__file__" in locals() else os.getcwd()        # For keeping the project file location in memory

if path.exists(path.join(project_path, text_name)):                                     # For checking if the text file exists
    text_file_open = open(path.join(project_path, text_name), 'r')
    text_to_parse = text_file_open.read()
    text_file_open.close()
    print(f"\nText file successfully found.\n")
else:
    print(f"\nText file not found.\n")
    quit()

print(f"Tokenizing words and calculating the frequencies...\n")                         # Tokenize the words in the imported text
parse_timer_start = time.time()
word_tokens = word_tokenize(text_to_parse)

word_frequencies = {}                                                                   # Count frequencies of every word in the text and weigh it
for word in word_tokens:    
    if word.lower() not in stop_words:
        if word.lower() not in punctuation:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

max_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word] / max_frequency

print(f"Tokenizing sentences and calculating the frequencies...\n")                     # Tokenize the sentences in the imported text
sentence_tokens = sent_tokenize(text_to_parse)

sentence_frequencies = {}                                                               # Count frequencies of every sentence in the text and weigh it
for sent in sentence_tokens:
    sentence = sent.split(" ")
    for word in sentence:        
        if word.lower() in word_frequencies.keys():
            if sent not in sentence_frequencies.keys():
                sentence_frequencies[sent] = word_frequencies[word.lower()]
            else:
                sentence_frequencies[sent] += word_frequencies[word.lower()]

print(f"Summarizing...\n")                                                              # Get the top 30% of the weighted sentences and create the summary
select_length = int(len(sentence_tokens) * 0.3)

summary = nlargest(select_length, sentence_frequencies, key = sentence_frequencies.get)

with open(output_name, 'w') as output:                                                  # Save summary to text file
    for line in summary:
        output.write(line)
        output.write('\n\n')

parse_timer_end = time.time() - parse_timer_start

summary_to_character = [word for word in summary]
summary = ' '.join(summary_to_character)

if path.exists(path.join(project_path, output_name)):                                   # Print results for user
    print(f"File successfully saved as '{output_name}'.\n")
    print(f"Original text was {len(text_to_parse)} characters long.")
    print(f"Summarized text is {len(summary)} characters long.")
    print(f"Summarization of text took {parse_timer_end:.3f} seconds.\n")