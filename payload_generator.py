num=int(input("Enter the total character : "))
file=open("payload.txt","a")
list_item=[]
for i in range(0,num):
    inputs=input("Enter the character : ")
    list_item.append(inputs)
for j in range(0,num):
    for k in range(0,num):
        for l in range(0,num):
            file.write(list_item[j])
            file.write(list_item[k])
            file.write(list_item[l])
            file.write("\n")
file.close()
file=open("payload.txt","r")
file.read()
