
import string
from math import log2 as log
from collections import OrderedDict

global corpus, corpus_size, unigrams, bigrams, words
corpus = 'tweets_'
unigrams = {}
bigrams = {}
words = []
corpus_size = 0 #number of total characters
num_lines = 0 #number of total lines

def calculate_size():
    global corpus_size, num_lines
    # First, calculate number of lines
    print('Calculating strings in corpus:')
    num_lines = sum(1 for line in open(corpus))
    print('{:,d} strings (lines)'.format(num_lines))
    lines_read = 0
    round_percs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # Second, calculate number of characters
    print('Calculating total characters in corpus:')
    with open(corpus, 'r') as data:
        for line in data:
            lines_read += 1
            perc = lines_read / num_lines
            if perc > round_percs[0]:
                print('{0} % calculated...'.format(round_percs.pop(0) * 100))
            for char in line:
                if char in string.ascii_lowercase:
                    corpus_size += 1
    print('Number of characters: {:,d}'.format(corpus_size))

def get_unigrams():
    global unigrams
    # Calculate frequency of each character
    print('Calculating frequency of characters...')
    with open(corpus, 'r') as data:
        for line in data:
            for char in line:
                if char in string.ascii_lowercase:
                    if char not in unigrams.keys():
                        unigrams[char] = 1
                    else:
                        unigrams[char] += 1
        data.close()
    print('Done. Number of unigrams: {:,d}'.format(len(unigrams)))
    # Calculate probability of each character from frequency
    print('Calculating probability of characters...')
    for char in unigrams.keys():
        unigrams[char] = unigrams[char] / corpus_size
    # Sort results and write into file
    probabilities = list(unigrams.values())
    probabilities.sort(reverse=True)
    print('Done. Writing results to disk...')
    with open('unigrams', 'w') as output:
        for p in probabilities:
            output.write(list(unigrams.keys())[list(unigrams.values()).index(p)] + ' ' + str(p) + '\n')
        output.close()
    print('Completed. Results in output file.')
    dist = sum(probabilities)
    print('Sum of all probabilities: {}'.format(dist))

def get_tokens():
    global words, num_lines
    print('Calculating tokens in corpus...')
    wordnum = 0
    lines_read = 0
    round_percs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    with open(corpus, 'r') as data:
        for line in data:
            if lines_read == 10000:
                break
            line = line.split()
            lines_read += 1
            perc = lines_read / 10000 #lines_read
            if perc > round_percs[0]:
                print('{0} % calculated...'.format(round_percs.pop(0) * 100))
            if line:
                for word in line:
                    if not word.isspace():
                        wordnum += 1
                        if word not in words:
                            words.append(word)
    print('Done. {:,d} tokens, {:,d} words.'.format(wordnum, len(words)))
    print('Writing words to disk...')
    with open('rawwords', 'w') as output:
        for w in words:
            output.write(w + '\n')
        output.close()
    print('Completed. Results in output file.')

def get_unigram_probability():
    global unigrams, words
    unigram_words = {}
    print('Calculating log probability of words...')
    for word in words:
        psum = 0.0
        plog = 0.0
        for char in word:
            psum += -1 * log(unigrams[char])
        plog = psum / len(word)
        unigram_words[word] = plog
    print('Done. Writing log probabilities to disk...')
    ordered_plogs = OrderedDict(sorted(unigram_words.items(), key=lambda t: t[1]))
    with open('plog_words', 'w') as output:
        for w, p in ordered_plogs.items():
                output.write(w + ' ' + str(p) + '\n')
        output.close()
    print('Congratulations. All done')

def get_bigrams():
    pass

def clean_memory():
    del corpus,
    del unigrams
    del bigrams
    del words

if __name__ == '__main__':
    calculate_size()
    get_unigrams()
    get_tokens()
    get_unigram_probability()
