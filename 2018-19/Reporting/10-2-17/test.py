outputFile = open("output.csv", "w")

openers = open("opened_search_email.csv", "r")
listA = [] #list of purls

for line in iter(openers):
  data = line.split(",")
  listA.append(data[0])

nonLanders = open("non_landers.csv", "r")
listB = [] #list of purls
listC = [] #list of contacts with data

for line in iter(nonLanders):
  listC.append(line)
  listB.append(line.split(",")[0])

for i in listA:
  try:
    outputFile.write(listC[ listB.index(i) ])
  except ValueError:
    continue