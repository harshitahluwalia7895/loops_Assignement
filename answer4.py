l1=['iphone',200,30.23,'Samsung','Nokia',10000,6623.98,11123,'Google',1231.0,'vivo',5000]
l2=[]
l3=[]
l4=[]

for index in range(len(l1)):
	if type(l1[index])==str:
		l2.append(l1[index])
	elif type(l1[index])==int:
		l3.append(l1[index])
	elif type(l1[index])==float:
		l4.append(l1[index])
print(l2)
print(l3)
print(l4)
