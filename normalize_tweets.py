"""
Input is file with tweets in the following format:
DATE    TIMESTAMP   ID  USER    USERNAME TWEET
Returns only the tweet, removes punctuations, words in non-latin alphabet and hashtags.
"""

import string

corpus = 'tweets'
normalized_corpus = 'tweets_'
removepunct = str.maketrans('', '', string.punctuation)
round_percs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

def normalize():
    lines = 0
    with open(corpus, 'r') as data, open(normalized_corpus, 'w') as normalized_data:
        num_lines = sum(1 for line in open(corpus))
        for line in data:
            new_line = []
            split_line = line.split('	')[-1]
            for word in split_line.split():
                word = word.translate(removepunct)
                if word.isalpha() and '@' not in word and '#' not in word and '[newline]' not in word:
                    is_latin_only = True
                    for char in word.lower():
                        if char not in string.ascii_letters:
                            is_latin_only = False
                            break
                    if is_latin_only:
                        new_line.append(word.lower())
            if len(new_line) != 0:
                normalized_data.write(' '.join(new_line) + '\n')
                lines += 1
            #Print progress in cosole
            perc = lines / num_lines
            if perc > round_percs[0]:
                print('{0} % calculated...'.format(round_percs.pop(0) * 100))
    print('Completed: {:,d} lines normalized'.format(lines))

if __name__ == '__main__':
    normalize()


#2016-05-17 01:41:21 +0200	732355286355333121	@r1960b	Roman B	I have no problem with this, Anderson did not deserve to hang around for a win
