import re
hand = open('mbox-short.txt')

#for line in hand:
    #line = line.rstrip()
    #if line.find('From:') >= 0 :
    #    print(line)

    #if re.search('^X-\S+:',line):
    #    print(line)

    #if re.search('[A-Z][0-9]+',line):
    #   print(line)

    #print(re.findall('[0-9]+',line))

    #print(re.findall('^F.+:',line))

#x = 'My 2 favourite numbers are 19 and 42'
#y = re.findall('[0-9]+',x)

#print(y)

#x = 'From: Using the : character'
#print(re.findall('^F.+:',x)) #greedy match
#print(re.findall('^F.+?:',x)) #non-greedy match
