import random
import sys

def readFile(fname):
  with open(fname, "r") as fin:
    lines = fin.readlines()
    lines = [line.strip() for line in lines]
    return lines

def printBanner(msg):
  stars = "*" * (len(msg) + 4)
  print(stars)
  print("* " + msg + " *")
  print(stars)

def printTurn(participant, topic):
  printBanner("Participant : " + participant)
  printBanner("Topic : " + topic)

topics = readFile("topics.txt")
doneTopics = readFile("done.txt")

remainingTopics = [topic for topic in topics if topic not in doneTopics]

if(remainingTopics == []):
  print("All topics done!")
  sys.exit(0)

participants = ["Diva", "Vigyan", "Udayan", "Vidyut", "Sujit"]
participantNum = random.randint(0, len(participants) - 1)
topicNum = random.randint(0, len(remainingTopics) - 1)
participant = participants[participantNum]
topic = remainingTopics[topicNum]
with open("done.txt", "a+") as fout:
  fout.write(topic + "\n")

printTurn(participant, topic) 
