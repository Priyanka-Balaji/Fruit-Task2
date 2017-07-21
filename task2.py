import csv
fnum=open('number.csv','r')
ffruits=open('fruits.csv','r')
fprice=open('price.csv','r')
frotten=open('rotten.csv','r')
dict_fruits=dict()
reader=csv.reader(fnum,delimiter=' ',quotechar=',')
for row in reader:
	l=(row[0].split(','))
for i in range(100):
	if l[i]!='':
		dict_fruits.update({int(l[i]):{'ID':int(l[i])}})
list_a=list(dict_fruits.keys())
for i in range(101):	
	if i%2!=0 and i not in list_a:
		dict_fruits.update({i:{'ID':i}})
list_keys=list(dict_fruits.keys())	
del l
del list_a
fnum.close()
reader=csv.reader(ffruits,delimiter=' ',quotechar=',')
for row in reader:
	l=(row[0].split(','))
for i in range(len(l)):
	if i not in list_keys:
		del l[i]
for i in range(len(l)):
	if l[i]=='':
		l[i]=l[i-10]
for i in range(len(dict_fruits)):
	j=list_keys[i]
	dict_fruits[j]['Name']=l[i]	
del l
ffruits.close()
reader=csv.reader(fprice,delimiter=' ',quotechar=',')
for row in reader:
	l=(row[0].split(','))
for i in range(len(dict_fruits)):
	j=list_keys[i]
	if l[i]=='':
		dict_fruits[j]['Price']=float(0)
	else :
		dict_fruits[j]['Price']=float(l[i])
del l
fprice.close()
reader=csv.reader(frotten,delimiter=' ',quotechar=',')
for row in reader:
	l=(row[0].split(','))
for i in range(len(l)):
	if l[i]=='1' :
		l[i]='t'
	elif l[i]=='0':
		l[i]='f'
	else:
		continue
for i in range(len(dict_fruits)):
	j=list_keys[i]
	dict_fruits[j]['Rotten']=l[i]
	if l[i]=='t':
		dict_fruits[j]['Price']=float(0)
frotten.close()
fwrite=open('new.csv','w')
writer=csv.writer(fwrite)
for i in dict_fruits:
	writer.writerow([dict_fruits[i]['ID'],dict_fruits[i]['Name'],dict_fruits[i]['Price'],dict_fruits[i]['Rotten']])        
#print(dict_fruits)

