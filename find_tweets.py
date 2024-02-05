import re

buzzwords = ["Trump", "President", "Joe Biden", "Donald Trump", "Chris Wallace", "Biden", "Joe", "JoeBiden," "@joebiden"]
t = open("presidential_debate_tweets.txt", "w")
with open("presidential_debate.txt", "r") as f:
    for line in f.readlines():
        i = 0
        while i < len(buzzwords):
            x = re.findall(buzzwords[0], line)
            if len(x) != 0:
                t.write(line)
                break
            i += 1

t.close()
f.close()

    