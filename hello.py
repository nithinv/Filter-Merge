


import csv
reader1 = csv.reader(open('C:\\Users\\nithin\\Desktop\\data1.csv', 'rb'), delimiter=',', quotechar='"')
row11 = reader1.next()

reader2 = csv.reader(open('C:\\Users\\nithin\\Desktop\\data2.csv', 'rb'), delimiter=',', quotechar='"')
row21 = reader2.next()

print row21    

writer1 = csv.writer(open('C:\\Users\\nithin\\Desktop\\sample.csv', 'wb'), delimiter=',', quotechar='"')
writer1.writerow(row21)   

while True:

	row12 = reader1.next()

	list = [];
	length = len(row21)
	for i in range(0, length):
		x = row21[i]
		y = x[1] 
		#print y
		list.append(row12[int(y) - 1]);
        print list    
        writer1.writerow(list)
	