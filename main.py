unique_words = set() #создание пустого множества уникальных слов
with open('text.txt','r') as infile: #чтенике из файла и проверка на уникальность
    for line in infile:
        words=line.split()
        for word in words:
            unique_words.add(word)
with open('output.txt','w') as outfile: #запись в файл
    for word in unique_words:
        outfile.write(word+' ')
