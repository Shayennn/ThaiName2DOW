f = open('testdata.csv', 'r')
for line in f.readlines():
    name, birthday = line.split(',')
    data_f = open('datasets/'+name, 'w')
    data_f.write(birthday)
    data_f.close()
