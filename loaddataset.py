f = open('testdata.csv', 'r')
for line in f.readlines():
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    name, birthday = line.split(',')
    year = int(birthday[-4:])-543
    data_f = open('datasets/'+name, 'w')
    data_f.write(birthday[0:4]+str(year))
    data_f.close()
