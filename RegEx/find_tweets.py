import re

def find_all_tweets(file):
    tweets = 0
    buzzwords = ["[Tt]rump", "@[Dd]onald[Tt]rump", "[Pp]resident", "[Dd]onald[Tt]rump", "[Jj]oe [Bb]iden", "[Dd]onald [Tt]rump", "[Cc]hris [Ww]allace", "[Cc]hris[Ww]allace", "@[Cc]hris[Ww]allace", "[Bb]iden", "[Jj]oe", "[Jj]oe[Bb]iden," "@[Jj]oe[Bb]iden"]
    t = open(file, "w")
    with open("presidential_debate.txt", "r") as f:
        for line in f.readlines():
            i = 0
            while i < len(buzzwords):
                x = re.findall(buzzwords[i], line)
                if len(x) != 0:
                    t.write(line)
                    tweets += 1
                    break
                i += 1
    t.close()
    f.close()
    return "There are " + str(tweets) + " tweets about the presidential debate in total."

def find_pres_tweets(file): 
    tweets = 0
    buzzwords = ["[Tt]rump", "@[Dd]onald[Tt]rump", "[Pp]resident", "[Dd]onald[Tt]rump", "[Jj]oe [Bb]iden", "[Dd]onald [Tt]rump", "[Cc]hris [Ww]allace", "[Cc]hris[Ww]allace", "@[Cc]hris[Ww]allace", "[Bb]iden", "[Jj]oe", "[Jj]oe[Bb]iden," "@[Jj]oe[Bb]iden"]
    t = open(file, "w")
    with open("presidential_debate.txt", "r") as f:
        for line in f.readlines():
            i = 0
            while i < len(buzzwords):
                x = re.findall(buzzwords[i], line)
                if len(x) != 0:
                    t.write(line)
                    tweets += 1
                    break
                i += 1
    t.close()
    f.close()
    return "There are " + str(tweets) + " tweets about the presidential debate that reference Joe Biden, Donald Trump, and Chris Walllace."


# print(find_all_tweets("all_tweets.txt"))
print(find_pres_tweets("presidential_debate_tweets.txt"))

    