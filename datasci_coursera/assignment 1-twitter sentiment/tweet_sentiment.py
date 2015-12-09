import sys
import json

# read sentiment file and return a dict with {word:score}
def read_sentiment_score(sentiment_file):
    afinnfile = open(sentiment_file)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    afinnfile.close()
    return scores
    
# calculate sentiment from input text
def calc_text_sentiment(text, sent_dict):
    words = unicode(text).split()
    text_score = 0.0
    for word in words:
        each_score = sent_dict.get(word, 0.0)
        text_score += each_score
    return text_score
    
# calculate sentiment from entire tweet file
def calc_tweet_sentiment(tweet_file, sent_dict):
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line, 'utf-8')
            if 'text' in tweet.keys():
                score = calc_text_sentiment(tweet['text'], sent_dict)
                print score
            


def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    sent_dict = read_sentiment_score(sent_file)
    calc_tweet_sentiment(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
