import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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
    state_sent = {}
    with open(tweet_file) as tf:
        for line in tf:
            tweet = json.loads(line, 'utf-8')
            if 'text' in tweet.keys():
                score = calc_text_sentiment(tweet['text'], sent_dict)
                location = tweet['user']['location'].replace(' ', '')
                state = convert_location_to_state_abbr(location)
                
                if state in state_sent:
                    state_sent[state].append(score)
                else:
                    state_sent[state] = [score]
    get_happiest_state(state_sent)
    
def convert_location_to_state_abbr(location):
  if ',' in location: # the two letters after comma is the state abbr.
    locterm = location.split(',')
    state = locterm[-1]
  else:
    state = location    
  # if state name is not abbreviated, find it in the state names map
  for abbr in states:
    if state[:4].lower() == states[abbr][:4].lower():
      return abbr
    if state == abbr:
      return abbr

def get_happiest_state(state_sent):
  max = -1
  happystate = 'xx'
  for state, scores in state_sent.items():
    sum = 0.0
    for score in scores:
      sum += score
    avg = sum / len(scores)
    if avg > max:
      happystate = state
      max = avg
  print happystate  

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    sent_dict = read_sentiment_score(sent_file)
    calc_tweet_sentiment(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
            