def matching(words):
    counter=0
    lst=[]
    for i in words:
       if len(i)>2 and i[0]==i[-1]:
           counter+=1
           lst.append(i)
    print("List of words which have first letter and last letter same",lst)
    return counter
counter=matching(["africa","of","and","mom","dad","but"])
print("Numbers of words having more than two characters and having first and last letters wich are same : ",counter)