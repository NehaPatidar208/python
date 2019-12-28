tup_1=(1,2,3,4)
tup_2=(4,5,6,7)
#concatenate
print("Concatenate",tup_1+tup_2)
#adding data have same index value
for i in range(0,len(tup_1)):
    print("sum of %d index values"%i,tup_1[i]+tup_2[i]);
print(tup_1[1:4]) #tuple values from index no 1 to index no 4
tup_3=tup_1+tup_2
print("length of tup_3 :",len(tup_3))
print("maximum value in tup_1",max(tup_1))
print("minimum value in tup_2",min(tup_2))
print("sum of all values of tup_1",sum(tup_1))
