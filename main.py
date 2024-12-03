unique_words=set()
with open('text.txt','r') as infile:
    for line in infile:
        words=line.split()
        for word in words:
            unique_words.add(word)
with open('output.txt','w') as outfile:
    for word in unique_words:
        outfile.write(word+' ')