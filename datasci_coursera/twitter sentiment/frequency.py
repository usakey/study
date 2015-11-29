import sys
import json

def decode_tweet_text(tweet_file):
    uncoded = []
    decoded = []
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line)
            #if tweet.has_key('text'):
            if 'text' in tweet.keys():
                uncoded.append(tweet['text'])
        for line in uncoded:
            decoded.append(line.encode('utf-8'))
    return decoded

def calc_tweet_freq(decoded_tweet):
    total_words_count = 0.0
    ## map contains word(K)->count(V)
    word_count = {}
    for line in decoded_tweet:
        for word in line.split():
            total_words_count += 1
            if word in word_count:
                word_count[word] += 1
            elif word.isalnum():
                word_count[word] = 1
    for i in range(len(word_count)):
        print word_count.keys()[i], word_count.values()[i]/total_words_count
    
def main():
    tweet_file = sys.argv[1]
    decoded_tweet = decode_tweet_text(tweet_file)
    calc_tweet_freq(decoded_tweet)
    #calc(x)
    
if __name__ == '__main__':
    main()