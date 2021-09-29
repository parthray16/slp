from nltk.corpus import udhr
from nltk.tokenize import RegexpTokenizer
import sys

def main() -> str:
    input_file = sys.argv[1]
    languages = ['Afrikaans', 'Danish_Dansk', 'Dutch_Nederlands',
                 'English', 'French_Francais', 'German_Deutsch', 
                 'Indonesian', 'Italian', 'Spanish', 
                 'Swedish_Svenska']
    words_dict = dict()
    # create a word bank for each lang
    for lang in languages:
        words_dict[lang] = set(udhr.words(lang + "-Latin1"))
    # tokenize input file
    tokenizer = RegexpTokenizer(r'\w+')
    file = open(input_file, 'r')
    file_words = set()
    for line in file:
        file_words.update(tokenizer.tokenize(line))
    file.close()
    # take set diff to see which lang has most words in common
    min_diff = sys.maxsize
    for lang in languages:
        difference = len(file_words - words_dict[lang])
        if difference < min_diff:
            min_diff = difference
            sim_lang = lang
    return sim_lang


    
if __name__ == "__main__":
    print(main())