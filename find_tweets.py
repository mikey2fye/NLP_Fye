import re

buzzwords = ['Trump', "President", "Joe Biden", "Donald Trump"]
t = open("presidential_debate_tweets.txt", "w")
with open("presidential_debate.txt", "r") as f:
    for line in f.readlines():
        x = re.findall("Trump", line)
        if len(x) != 0:
            t.write(line)
t.close()
f.close()

    