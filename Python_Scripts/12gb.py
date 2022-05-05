import pandas as pd
import re
import string
import json
import ast
from textblob import TextBlob
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords as stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def removeBrackets(comment):
    return re.sub('\[.*?\]', '', comment)

def removePunctuation(comment):
    return re.sub('[%s]' % re.escape(string.punctuation), '', comment)

def removeAlphaNum(comment):
    return re.sub('\w*\d\w*', '', str(comment))

def word_count(stringToSplit):
    counts = dict()
    stringToSplit = str(stringToSplit)
    words = stringToSplit.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def findMostUsedWord(dictionary):
    dictionary = ast.literal_eval(dictionary)
    mostUsed = max(dictionary, key=dictionary.get)
    mostDict = dict()
    mostDict[mostUsed] = dictionary.get(mostUsed)
    return mostDict

def wordCloudDict(row):
    row = ast.literal_eval(row)
    if list(row)[0] in wordCount:
        wordCount[list(row)[0]] = wordCount[list(row)[0]] + row.get(list(row)[0])
    else:
        wordCount[list(row)[0]] = row.get(list(row)[0])

df = pd.DataFrame()
wordCount = dict()

# this code block extracts the body field of our dataset, where the meat of our data is
'''df = pd.DataFrame()
df = pd.read_csv('the-reddit-covid-dataset-comments.csv', sep =",", header=0, usecols=[7])
df.to_csv('testfile')'''

# this code block is to make all our data lowercase
#df = pd.read_csv('body', sep =",", header=0, index_col=[0])
#df['body'] = df['body'].apply(str.lower)
#df.to_csv('lowerbody', header='body', index=True)

#this code block is to remove brackets from our data
'''df = pd.read_csv('lowerbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(removeBrackets)
df.to_csv('nobracketsbody', header='body', index=True)'''

#this code block removes punctuation
'''df = pd.read_csv('nobracketsbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].str.replace(r'[^\w\s]+', '')
df.to_csv('nopunctuationbody', header='body', index=True)'''

#this code removes words containing numbers
'''df = pd.read_csv('nopunctuationbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].str.replace(r'\w*\d\w*', '')
df.to_csv('noalphanumbody', header='body', index=True)'''

#this code removes some additional punctuation that might have been missed earlier
'''df = pd.read_csv('noalphanumbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].str.replace('[‘’“”…]', '')
df.to_csv('secondpunctuationpassbody', header='body', index=True)'''

#clean up non-sensical text here
'''df = pd.read_csv('secondpunctuationpassbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].str.replace('\n', '')
df.to_csv('nonsensicalbody', header='body', index=True)'''

#we are going to remove stop words by using the nltk package
'''df = pd.read_csv('nonsensicalbody', sep =",", header=0, index_col=[0])
stop = stopwords.words('english')
df['body'] = df['body'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in stop]))
df.to_csv('removestopwordsbody', header='body', index=True)'''

# we want to get the word counts per row here
'''df = pd.read_csv('file_part_00', sep =",", header=0, index_col=[0])
resultSet = df['body'].str.split().apply(pd.value_counts)
resultSet.to_csv('file_part_00_wordcountbody', header='body', index=True)'''

# another attempt to count words using Counter
'''df = pd.read_csv('file_part_00', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_00_wordcountbody', header='body', index=True)'''

# get the word used most in the row
'''df = pd.read_csv('file_part_00_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_00_mostusedwordbody', header='body', index=True)'''

# build a dictionary from all rows
df = pd.read_csv('9mill_count_body00', sep =",", header=0, index_col=[0])
wordCount = dict()
for index, row in df.iterrows():
    wordCloudDict(row['body'])
wordcloud = WordCloud(width=1000, height=500).generate_from_frequencies(wordCount)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud)
plt.show()

# adding header to each of the split files, now we need to test with pandas and apply word count
'''df = pd.read_csv('file_part_01new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_01_wordcountbody', header='body', index=True)'''


# I want to apply a sentiment value to each row, given the most used word per row
'''df = pd.read_csv('mostusedwordbody', sep =",", header=0, index_col=[0])
pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('sentimentbody', header='body', index=True)'''

############################################################################################################################

############################################################################################################################

############################################################################################################################

'''WE ARE GOING TO BE PERFORMING THE SAME OPERATIONS ON THE REST OF THE FILES
    STARTING WITH FILE_PART_01'''

# file_part_01 most used word
'''df = pd.read_csv('file_part_01_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_01_mostusedwordbody', header='body', index=True)'''

# file_part_02 word count
'''df = pd.read_csv('file_part_02new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_02_wordcountbody', header='body', index=True)'''

# file_part_02 most used word
'''df = pd.read_csv('file_part_02_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_02_mostusedwordbody', header='body', index=True)'''

# file_part_03 word count
'''df = pd.read_csv('file_part_03new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_03_wordcountbody', header='body', index=True)'''

# file_part_03 most used word
'''df = pd.read_csv('file_part_03_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_03_mostusedwordbody', header='body', index=True)'''

# file_part_04 word count
'''df = pd.read_csv('file_part_04new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_04_wordcountbody', header='body', index=True)'''

# file_part_04 most used word
'''df = pd.read_csv('file_part_04_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_04_mostusedwordbody', header='body', index=True)'''

# file_part_05 word count
'''df = pd.read_csv('file_part_05new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_05_wordcountbody', header='body', index=True)'''

# file_part_05 most used word
'''df = pd.read_csv('file_part_05_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_05_mostusedwordbody', header='body', index=True)'''

# file_part_06 word count
'''df = pd.read_csv('file_part_06new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_06_wordcountbody', header='body', index=True)'''

# file_part_06 most used word
'''df = pd.read_csv('file_part_06_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_06_mostusedwordbody', header='body', index=True)'''

# file_part_07 word count
'''df = pd.read_csv('file_part_07new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_07_wordcountbody', header='body', index=True)'''

# file_part_07 most used word
'''df = pd.read_csv('file_part_07_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_07_mostusedwordbody', header='body', index=True)'''

# file_part_08 word count
'''df = pd.read_csv('file_part_08new', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(word_count)
df.to_csv('file_part_08_wordcountbody', header='body', index=True)'''

# file_part_08 most used word
'''df = pd.read_csv('file_part_08_wordcountbody', sep =",", header=0, index_col=[0])
df['body'] = df['body'].apply(findMostUsedWord)
df.to_csv('file_part_08_mostusedwordbody', header='body', index=True)'''

#results = pd.read_csv('the-reddit-covid-dataset-comments.csv')
#print("Number of lines: ", len(results))