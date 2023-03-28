'''marks=[15,5,10,-5]
for i in range(len(marks)):
    for j in range(i+1,len(marks)):
        if (marks[i]>marks[j]):
            marks [i],marks
    print(i,"=",marks[i],marks[i]==marks[j], marks[j])
print(marks)'''


'''key=int(input("Enter the key:"))
if key in marks:
        print("yes")
else:
    print("no")'''


marks=[15,5,10,-5,25,-5,25,10,-5]
l=[]
for i in range(len(marks)):
    c=1
    for j in range(i+1,len(marks)):
        if marks[i]==marks[j]:
            c+=1
    if marks[i] not in l:
                print(marks[i],"is repeated",c,"times")
                l.append(marks[i])
        
