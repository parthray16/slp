from nltk.corpus import gutenberg
from random import choice, randint
from nltk.tokenize import RegexpTokenizer, sent_tokenize
import re


def main():
    num_paragraphs = 3
    # tokenize sentences & paragraphs
    paragraphs = list(gutenberg.paras('bible-kjv.txt'))
    for i in range(len(paragraphs)):
        for j in range(len(paragraphs[i])):
            # add sentence marker
            paragraphs[i][j].insert(0, '<s>')
            paragraphs[i][j].append('</s>')
        # add paragraph marker
        paragraphs[i][0].insert(0, '<ps>')
        paragraphs[i][-1].append('</ps>')
    # remove punctuations and numbers
    tokenizer = RegexpTokenizer(r"[a-zA-Z_]+|<s>|</s>|<ps>|</ps>")
    filtered_words = tokenizer.tokenize(" ".join([word for paragraph in paragraphs for sent in paragraph for word in sent]))  
    
    #trigram paragraphs
    print('\nTrigram Paragraphs')
    for n in range(num_paragraphs):
        print('Paragraph %d:' % (n + 1))
        num_sentences = randint(2, 5)
        for i in range(num_sentences):
            sentence = ''
            if i == 0:
                prev_word1 = '<ps>'
                prev_word2 = '<s>'
            else:
                prev_word1 = '<s>'
                prev_word2 = ''  
            while prev_word2 != '</s>' and prev_word2 != '</ps>':
                # get first word with bigrams
                if (prev_word1 == '<s>' or prev_word1 == '<ps>') and prev_word2 == '':
                    prev_word2 = choice(bigram(prev_word1, filtered_words))
                    sentence += prev_word2 + ' '
                else:
                    prev_word1, prev_word2 = prev_word2, choice(trigram(prev_word1, prev_word2, filtered_words))
                    if prev_word2 != '</s>' and prev_word2 != '</ps>':
                        sentence += prev_word2 + ' ' 
            print(sentence + '\n')     
    return None
    

def bigram(prev_word, words):
    filtered_words = []
    size = len(words)
    for i in range(size):
        if words[i] == prev_word and i < size - 2:
            filtered_words.append(words[i + 1])
    return filtered_words


def trigram(prev_word1, prev_word2, words,):
    filtered_words = []
    size = len(words)
    for i in range(size):
        if i < size - 3 and \
           words[i] == prev_word1 and \
           words[i + 1] == prev_word2:
            filtered_words.append(words[i + 2])
    return filtered_words

    
if __name__ == "__main__":
    main()