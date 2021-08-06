from collections import Counter
list_words=[]
n=int(input("Enter Number of words : "))
for i in range (1,n+1):
    i=input("Enter Word : ")
    list_words.append(i)
# print(list_words)

#Converted Into set to get only Distinct Words
a=set(list_words)
print("Number Of Distinct Words : ",len(a))
# print(a)
# print(Counter(list_words))


Count =set(list_words)
x={count:list_words.count(count) for count in list_words}
print("Occurences of Each as per Input Order : ",x)





# BONUS PART
# Prints Occurences in Descending Order
descend = Counter(list_words).most_common()
print("Occurences in Descending Order : ",descend)


# Shows Most repeated Word
max_repeat = Counter(list_words).most_common(1)
print("Most Repeated Word : ", max_repeat)


#  Shows Least repeated Word
min_repeat =Counter(list_words).most_common()[-1]
print("Least Repeated Word : ", min_repeat)
