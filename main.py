
global corpus, corpus_size, unigrams, bigrams
corpus = 'tweets_'
unigrams = {}
bigrams = {}
corpus_size = 0 #number of total characters

def calculate_size():
    global corpus_size
    # First, calculate number of lines
    print('Calculating tweets in corpus:')
    num_lines = sum(1 for line in open(corpus))
    print('{:,d} tweets'.format(num_lines))
    lines = 0
    round_percs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # Second, calculate number of characters
    print('Calculating total characters in corpus:')
    with open(corpus, 'r') as data:
        for line in data:
            lines += 1
            perc = lines / num_lines
            if perc > round_percs[0]:
                print('{0} % calculated...'.format(round_percs.pop(0) * 100))

            for char in line:
                if char.isalpha():
                    corpus_size += 1
    print('Number of characters: {:,d}'.format(corpus_size))

def get_unigrams():
    global unigrams
    # Calculate frequency of each character
    print('Calculating frequency of characters...')
    with open(corpus, 'r') as data:
        for line in data:
            for char in line:
                if char not in unigrams.keys():
                    unigrams[char] = 1
                    print('Added: ', char)
                else:
                    unigrams[char] += 1
        data.close()
    # Calculate probability of each character from frequency
    print('Calculating probability of characters...')
    for char in unigrams.keys():
        unigrams[char] = unigrams[char] / corpus_size
    # Sort results and write into file
    probabilities = list(unigrams.values())
    probabilities.sort(reverse=True)
    with open('unigrams', 'w') as output:
        for p in probabilities:
            output.write(list(unigrams.keys())[list(unigrams.values()).index(p)] + ' ' + str(p) + '\n')
        output.close()
        print('Completed. Results in output file.')

def get_bigrams():
    # TODO

def sort_words():
    # TODO

if __name__ == '__main__':
    calculate_size()
    get_unigrams()
