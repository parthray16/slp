from nltk.corpus import gutenberg
from random import choice, randint
from nltk.tokenize import RegexpTokenizer, sent_tokenize

def main():
    num_sentences = 5
    # tokenize sentences
    sents = sent_tokenize(gutenberg.raw('austen-emma.txt')) + \
            sent_tokenize(gutenberg.raw('austen-persuasion.txt')) + \
            sent_tokenize(gutenberg.raw('austen-sense.txt'))
    tokenized_sents = ['<s> ' + sent + ' </s>' for sent in sents]
    # remove punctuations
    tokenizer = RegexpTokenizer(r"[\w]+|<s>|</s>")
    filtered_words = tokenizer.tokenize(" ".join(tokenized_sents))

    # bigram sentences
    print('Bigram Sentences')
    for n in range(num_sentences):
        print('Sentence %d:' % (n + 1))
        sentence = ''
        prev_word = '<s>'    
        while prev_word != '</s>':
            prev_word = choice(bigram(prev_word, filtered_words))
            if prev_word != '<s>' and prev_word != '</s>':
                sentence += prev_word + ' '
        print(sentence)

    #trigram sentences
    print('\nTrigram Sentences')
    for n in range(num_sentences):
        print('Sentence %d:' % (n + 1))
        sentence = ''
        prev_word1 = '<s>'    
        prev_word2 = ''
        while prev_word2 != '</s>':
            # get first word with bigrams
            if prev_word1 == '<s>' and prev_word2 == '':
                prev_word2 = choice(bigram(prev_word1, filtered_words))
                sentence += prev_word2 + ' '
            else:
                prev_word1, prev_word2 = prev_word2, choice(trigram(prev_word1, prev_word2, filtered_words))
                if prev_word2 != '</s>':
                    sentence += prev_word2 + ' '
        print(sentence)     
    return None
    

def bigram(prev_word, words):
    filtered_words = []
    size = len(words)
    for i in range(size):
        if words[i] == prev_word and i < size - 2:
            filtered_words.append(words[i + 1])
    return filtered_words


def trigram(prev_word1, prev_word2, words):
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