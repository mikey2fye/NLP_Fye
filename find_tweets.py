import re

def find_all_tweets(file):
    pass

def find_pres_tweets(file): 
    buzzwords = ["Trump", "@donaldtrump", "President", "DonaldTrump", "Joe Biden", "Donald Trump", "Chris Wallace", "Biden", "Joe", "JoeBiden," "@joebiden"]
    t = open(file, "w")
    with open("presidential_debate.txt", "r") as f:
        for line in f.readlines():
            i = 0
            while i < len(buzzwords):
                x = re.findall(buzzwords[i], line)
                if len(x) != 0:
                    t.write(line)
                    break
                i += 1
    t.close()
    f.close()


# find_all_tweets("all_tweets.txt")
find_pres_tweets("presidential_debate_tweets.txt")

    