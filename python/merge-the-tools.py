# Python>Strings>Merge the Tools!

#Given a string (s). Divide the string in group of k letters. Then print the letters of each subgroup without repeating the same letter in each subgroup.

#Ex:
# Sample Input: 
s = 'AABCAAADA'
k = 3 

#Sample Output:
# AB
# CA
# AD

#Solution:-------------

#Check if the string can be divide in n substrings, all of the same size (len(s)%k == 0)
if len(s)%k == 0:
    num_div = len(s)//k
else:
    num_div = len(s)//k + 1

#Iterate num_div times
for it in range(num_div):
    mylist = []
    #Create new substring with k lenght
    for letter in s[it*k:it*k+k] :
        mylist.append(letter)
    #Take only each letter once
    mylist = list(dict.fromkeys(mylist))
    myWord = ""
    #Transform from list with letters to string
    for item in mylist:
        myWord += item
    #Print one substring solution
    print(myWord)