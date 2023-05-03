# WAP to count character from file 
file = open("Rahul.txt", "r")

text = file.readlines()

count = 0

for i in text:
    for j in i:
        if(j != " " and j != "\n"):
            count+=1
            
print(count)