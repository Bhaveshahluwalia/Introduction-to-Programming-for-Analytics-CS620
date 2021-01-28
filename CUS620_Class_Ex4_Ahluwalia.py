#!/usr/bin/env python
# coding: utf-8

# # # CUS620, Class Exercise 3
# ## Your full name: Bhavesh Ahluwalia
# --------------
# - ### Note1: you can use this temaplet to answer questions such as class Exercise and HWs
# - ### Note2: chnage the file name respect to type of assignment, for example: CUS620_Class_Ex1_LastName or CUS620_HW1_LastName
# ---------
# ### if you need help on how to write in Jupyter see here: 
# - Jupyter notebook tutorial: [link](https://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb)
# - basic: [link](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
# - advance: [link](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting)

# pdf exercise question

# # 5 Tuples

# # Exercise 5.1: Swapping two values
# Suppose you have two variables: a and b. Now you want to set a equal to the value of b and at the same time set b equal to the value of a.
# 
# The following obviously does not work
# a=b 
# b=a
# 
# so in some languages, you need to define a third variable like this
# 
# t=a 
# a=b
# b=t
# 
# However, in Python you don’t need to do this. How can you swap a and b in one line?

# In[14]:



a=50
b=100
a,b = b,a #it takes the values of the right side by creating a tuple (b,a). Then this tuple is unpacked and assigned to the variables in the reverse order.
print ("After Swapping values of a =",a) 
print ("After Swapping values of b =",b) 


# # Exercise 5.2: Zip
# Suppose we have two lists, x and y that give the x and y coordinates of a set of points. Create a list with the coordinates (x,y) as a tuple. Hint: Find out about the zip function.
# 
# You have decided that actually, you need the two seperate lists, but unfortunately, you have thrown them away. How can we use zip to unzip the list of tuples to get two lists again?

# In[88]:


classno = ['Sql', 'Introduction to' , 'data'] 
classname = ['database', 'python', 'mining'] 
zipped = list(zip(classno, classname)) # this will join the each value of two list together in order form
print(zipped)


# In[89]:


res = list(zip(*zipped)) # here we can use unpacking operator * to unzip the data and print them separatly
print("Two lists of tuples After unzip the zip function \n ")
print (list(res))


# # Exercise 5.3: Distances
# Suppose we have two vectors, x and y, stored as tuples with n elements. Implement functions that compute the l1 and l2 distances between x and y. Note that n is not explicitly given.

# In[44]:


a=[9,8,7,6,5,9,8,9,9,0]
b=[1,2,3,4,5,6,7,8,9,0]


# In[45]:


# not sure about this coz n is not explicitly given.
def distance(a,b):
    for i in range(len(a)): # for loop since we donot know how long the n elements in x and y vector
        out= a[i]-b[i]
        print (out)
distance(a,b)


# # 7 File I/O

# Exercise 7.1: Open a file
# Write a function that opens a file (input: filename), and prints the file line by line.

# In[5]:


def openfile():
    inFile = input("enter name of input file> ")
    inf = open(inFile,'r')
    aa=inf.read()
    print(aa)
    
openfile()


# Exercise 7.2: Wordcount
# On the course website you can find a text file containing the complete works of William Shapespeare. (a) Find the 20 most common words
# (b) How many unique words are used?
# (c) How many words are used at least 5 times?
# (d) Write the 200 most common words, and their counts, to a file.

# In[49]:


def openfile():
    infile = open('shakespeare.txt','r' )
    aa=infile.read()
    print(aa)
    
openfile()


# In[4]:


#a) Find the 20 most common word
from collections import Counter # importing the library
with open('shakespeare.txt') as find:
    count = Counter(find.read().lower().strip().split()) #build a counter from each word in the file and change into to lowe and split them 

print(count.most_common(20))


# In[7]:


#version 2 
words = open('shakespeare.txt').read().lower().split()
from collections import Counter
count = Counter(words)
count.most_common(20)


# In[35]:


#(b)How many unique words are used?
words = open('shakespeare.txt').read().lower().split()
name=[] # creating vector
unique = [] # creating vector
for i in words: # for loop to run through each word
    name.append(i)# append to add the word in the end 
for j in name:
    if j not in unique: #if it is not unique then add in the end and count the words wih the count loop 
        unique.append(j)
count= 0
for k in unique:
    count= count+1 # here it count all the unique words 
print("Unique numbers in the file shakespeare.txt =  ", count)


# In[17]:


#version2 with function & with set() function
def unique_words(filename):
    wordSet = set()
    with open(filename, 'r') as f:
        for line in f:
            for word in line.lower().split():
                wordSet.add(word)
    f.close()
    print(len(wordSet))
unique_words("shakespeare.txt")


# In[75]:


#(c) How many words are used at least 5 times?
file= open('shakespeare.txt').read().lower().split()
counter={} #dictionary of the counter 
for word in file:
    if word in counter: #condition to check the words with counter 
        counter[word]=counter[word]+1 # count the words if it is exist 
    else: #else the count is 1 
        counter[word]=1 
atleast=[word1 for word1 in counter.values() if word1>=5] # this check is the word has atleast 5 numbers 
print("At least 5 numbers words in the file shakespeare.txt are" , len (atleast)) #print the words with which has atleast 5 numbers 


# In[33]:


#(d)Write the 200 most common words, and their counts, to a file.
with open('shakespeare.txt') as find:
    count = Counter(find.read().lower().strip().split()) #build a counter from each word in the file and change into to lowe and split them 
output= counter.most_common(200)
output

with open('7partd.txt', 'w') as out: # making a file called 7partd.txt to print the all 200 words with frequenies
    out.write(str(output))


# Exercise 7.4: Sum of lists
# Before you start coding, please read the entire problem.
# (a) Data generation
# Write a function that takes three integers, n, a and b and a filename and writes to the file a list
# with n random integers between a and b.
# (b) Reading the data
# Write a function that can read the files as generated above and return the values.
# 

# In[79]:


#(a) Data generation
#Write a function that takes three integers, n, a and b and a filename and writes to the file a list with n random integers between a and b.
import random 
def generate_data(n, a, b, filename): #n will take how many numbers you wanna print and a will where to start, b will where to end, filename take file we want to create 
    random_list = [] #making a vector to store int later 
    with open(filename, 'w') as w: #open the file to write in it where w means write
        while (n>0): # while loop to run when n is greater
            if (b > a): 
                randNumber = random.randint(a, b) # this will where to start and where to end like start from a and end with b 
                random_list.append(randNumber) # this will just add the number in the end. 
            elif (a > b): 
                randNumber = random.randint(b, a)
                random_list.append(randNumber)
            n = n - 1 # in each run 1 will minus from n number 
        w.write(str(random_list)) # write it in the file as a string
    w.close() #close the file 

generate_data(10, 1, 100, "question7.4.txt")


# In[82]:


#(b) Reading the data
#Write a function that can read the files as generated above and return the values.

def readfile(filename):
    infile = open(filename,'r' ) #open the file to read where r means read
    read_all=infile.read() # this is reading and put all values in read_all
    print(read_all) #here we print all the values
    
readfile("question7.4.txt")


# # book Exercise question

# # Chapter 5

# 5.12 Implement function test() that takes as input one integer and prints 'Negative',
# 'Zero', or 'Positive' depending on its value.
# >>> test(-3) Negative
# >>> test(0) Zero
# >>> test(3)
#    Positive

# In[94]:


def test(number):
    if number<0: # this will print negative is user put -value 
        print("Negative")
    elif number==0: # this will print zero is user put 0 
        print("Zero")
    else: # this will print positive is user put anything
        print("Positive")
test(-10)


# In[95]:


test(-3)


# In[96]:


test(0)


# In[97]:


test(3)


# 5.14 Write function mult3() that takes as input a list of integers and prints only the mul-
# tiples of 3, one per line.
# >>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])
# 3
# 6
# 3
# 9 
# 9

# In[98]:



def mult3(list):
    for number in list: #  for loop to go from beginning to end 
        if (number%3==0): # check if number goes to 3
            print(number) 
mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])


# 5.16 Implement function indexes() that takes as input a word (as a string) and a one- character letter (as a string) and returns a list of indexes at which the letter occurs in the word.
# >>> indexes('mississippi', 's') 
# [2, 3, 5, 6]
# >>> indexes('mississippi', 'i') 
# [1, 4, 7, 10]
# >>> indexes('mississippi', 'a') 
# []

# In[100]:


def indexes(string, character):
    listt=[] # making a vector for check each character
    for index, i in enumerate(string): #enumerate() method works as a adds a counter each run 
            if i== character: # this check which character is same as user put in char
                    listt.append(index) #this just add the number in the end 
    return listt
indexes('mississippi', 's')   


# In[13]:


indexes('mississippi', 'i')  


# In[14]:


indexes('mississippi', 'a')  #because there is no a in the string mississippi


# 5.18 Implement function four_letter() that takes as input a list of words (i.e., strings) and returns the sublist of all four letter words in the list.
# >>> four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']) ['stop', 'door', 'dust']

# In[103]:


def four_letter(list_of_words):
    a=[] # making a vector 
    for word in list_of_words: # run for loop for each words
        if len(word)==4: # this check if the sting list have 4 words
            a.append(word) # attach/add in the end
    return a
four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust'])


# In[104]:


four_letter(['dog', 'letter', 'stop', 'door', 'bust', 'dust', 'lust', 'cust'])


# 5.20 Write a function intersect() that takes two lists, each containing no duplicate values, and returns a list containing values that are present in both lists (i.e., the intersection of the two input lists).
# 
# >>> intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9])
# [3, 9]

# In[106]:


def intersect(list1,list2):
    b=[] # making b vector 
    for list_1_number in list1: # this will run the list 1
        for list_2_number in list2: # this will run the list 2
            if list_1_number==list_2_number: #this check list1 vector with list2 vector and then return the vector
                b.append(list_1_number) # this just add the vector in the end
    return b
intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9])
        


# In[108]:


intersect([1, 2, 3, 4, 5], [4, 3, 2, 1, 0])


# 5.22 Implement the function pairSum() that takes as input a list of distinct integers lst and an integer n, and prints the indexes of all pairs of values in lst that sum up to n.
# >>> pairSum([7, 8, 5, 3, 4, 6], 11) 
# 0 4
# 1 3
# 2 5

# In[112]:


def pairSum(lst,n):
    for a in range(0,len(lst)): # this will run from 0 to lst which is input by user
        for b in range(a+1,len(lst)): # this will run from lst +1 and end with the length of user lst
            if lst[a]+lst[b]==n:# this add  list i and list k and check if it is equal to 11 
                print(a,b)  
pairSum([7, 8, 5, 3, 4, 6], 11)
    


# 5.24 Write function case() that takes a string as input and returns 'capitalized', 'not capitalized', or 'unknown', depending on whether the string starts with an uppercase letter, lowercase letter, or something other than a letter in the English alphabet, respectively.
# >>> case('Android') 'capitalized'
# >>> case('3M') 'unknown'

# In[20]:


def case(strr):
    
    if strr[0]>="a":
        return "not capitalized"
    
    if strr[0]>="A":
        return "capitalized"
    
    else:
        return"unknown"

case('Android')


# In[21]:


case('3M')


# In[22]:


case('cus620')


# In[ ]:


#5.26 excluded by professor


# 5.28 Write function geometric() that takes a list of integers as input and returns True if the integers in the list form a geometric sequence. A sequence a0, a1, a2, a3, a4, . . . , an −2, an − 1 is a geometric sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3, . . . , an−1/an−2 are all equal.
#    >>> geometric([2, 4, 8, 16, 32, 64, 128, 256])
#    True
#    >>> geometric([2, 4, 6, 8])
#    False

# In[24]:


def geometric(listt):
    half= listt[1]/listt[0] #we divide the next vector of list with the vector of first and store in variable
    for i in range(1,len(listt)): #for loop which start from 1 to length of the list
        if listt[i]/listt[i-1] !=half: #we check if the list vector of i divide with list vector of i-1 is not equal of the variable we made then it is false else it is true
            return False
    if len(listt)<2: #this check the if length of list is less than 1 than retutn true
        return True
    return True


geometric([2, 4, 8, 16, 32, 64, 128, 256])


# In[25]:


geometric([2, 4, 6, 8])


# 5.30 Develop the function many() that takes as input the name of a file in the current directory (as a string) and outputs the number of words of length 1, 2, 3, and 4. Test your function on file sample.txt.
# >>> many('sample.txt') 
# Words of length 1 : 2 
# Words of length 2 : 5 
# Words of length 3 : 1 
# Words of length 4 : 10

# In[15]:


def many(filename):
    w_dict=dict()# dictionary of counters assigning as a varriable 
    with open(filename)as f:
        for line in f.readlines(): #readlines() read all lines in the file, as a list
            for word in line.split(): # split text into list of words
                word_len=len(word) # checj the length of word
                if word_len<=4: # condition where the word length is less than or equal to 4 
                    w_dict[word_len]=w_dict.get(word_len, 0)+ 1
                    
    return w_dict

many('sample.txt')


# In[138]:


# professor code given for practice 
def wordCount(text): 
    wordList = text.split()  # split text into list of words
    counters ={}             # dictionary of counters
    for word in wordList:   
        if word in counters: # counter for word exists
            counters[word] += 1
        else:                # counter for word doesn't exist
            counters[word] = 1
    for word in counters:    # print word counts
        if counters[word] == 1:
            print('Words of length {} : {} '.format(word, counters[word]))
        else:
            print('Words of length {} : {} '.format(word, counters[word]))
text = open('sample.txt').read()
wordCount(text)


# 5.32 Implement function fib() that takes a nonnegative integer n as input and returns the nth Fibonacci number.
#    >>> fib(0)
#    1
#    >>> fib(4)
#    5
# >>> fib(8) 
# 34

# In[5]:


def fib(number):
    if number<2: #we know if n<2 which has no more fibonacci so it return 1 
        return 1
    else:
        answer= fib(number-1)+fib(number-2) #we minus 1 and then minus from fib(number) then sum both to get Fibonacci
        return answer

fib(0)


# In[6]:


fib(4)


# In[7]:


fib(8)


# 5.34 Write a function statement() that takes as input a list of floating-point numbers, with positive numbers representing deposits to and negative numbers representing withdrawals from a bank account. Your function should return a list of two floating-point numbers; the first will be the sum of the deposits, and the second (a negative number) will be the sum of the withdrawals.
# >>> statement([30.95, -15.67, 45.56, -55.00, 43.78]) 
# [120.29, -70.67]

# In[36]:


def statement(list_numbers):
    deposit=0
    withdrawal = 0
    for number in list_numbers:
        if number>0:# if the n is bigger than 0; than with for loop we add all the deposits and return deposit 
            deposit=deposit+number
        else:
            withdrawal= withdrawal+number # here we add all the withdrawals and return it 
    return [deposit,withdrawal]

statement([30.95, -15.67, 45.56, -55.00, 43.78])


# In[ ]:


#5.36  excluded by professor


# 5.38 Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence:
#             x/2 ifxiseven 
# x=        3x+1 ifxisodd.
# 
# 
# 
# 
# Your function should stop when the sequence gets to number 1. Note: It is an open question whether the Collatz sequence of every positive integer always ends at 1.
#    >>> collatz(10)
#    10
#    5
#    16
# 8 4 2 1

# In[37]:


def collatz(integer):
    print(int(integer)) # first we just print the n as a interger 
    while integer!=1: # so, with while loop we check if n is not equal to 1 
        if integer%2==0: #then we check if it's even and take half of it 
            integer=integer/2
        else: # else we multiply n with 3 and add 1 then print it
            integer=3*integer+1
        print(int(integer))
collatz(10)


# In[ ]:




