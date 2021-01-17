#Part 1:
def rh_get_match(X, Y, k):
    #created empy tuples list so later we can append values in 
    tuples = []
    #we calculated the number of unique characters from two substrings X and Y.
    #set() will provide the unique characters from input. For instance, x ="learninglearninghoc". 
    #set(x) will give only unique characters such as {'a', 'c', 'e', 'g', 'h', 'i', 'l', 'n', 'o', 'r'}
    #Calculating the number of unique characters is essential for the later usage of hash function.
    d = len(set(X+Y))    
    #initialize the value and use those variables to update,store the rolling hash value of substrings length k from 
    #both string X and Y.
    hash_value_x = 0
    hash_value_y = 0
    
    # hash table to store substrings and their indexes
    # Ensuring the hash table is at least 60% full
    table_size = int((len(X)-k) / 0.6)
    
    q = 99999
    #helps the hashing to compute in the constant time
    h = d**(k-1) % q
    #create a 2D table
    h_table_x = [[] for i in range(table_size)]
    #using for loop and rolling hashing method to calculate the value of the substring_k
    for i in range(k):
        hash_value_x = (d*hash_value_x + ord(X[i])) % q
    #after calculating the hash_value of the substring_k, we append the substring having length
    #k into the hash_table with index calculated by hash_value of substring-k
    #divided by table_size.
    h_table_x[hash_value_x % table_size].append((X[:k], 0))
    
    #for loop for calculating the value of consecutive substring
    #and append the substring into the hash table
    for i in range(1, len(X)-k+1):
        sub = X[i:i+k]
        hash_value_x = (d*(hash_value_x - ord(X[i-1])*h) + ord(X[i+k-1])) % q
        h_table_x[hash_value_x % table_size].append((sub, i))
    #this loop is used to calculate the value of substring size k
    for j in range(k):
        hash_value_y = (d*hash_value_y + ord(Y[j])) % q
    
    
    if h_table_x[hash_value_y % table_size]:
        for word in h_table_x[hash_value_y % table_size]:
            if word[0] == Y[:k]:
                tuples.append((word[1], 0))
    #after calculating the value of substring size k
    #check whether the value of substring size k from string y has appeared 
    # or equal to any hash value of substring size k from string x.
    #if there is some value equivalent
    #check for all subtrings stored in the list.
    #if the any substring equals to substring from string y.
    #append them into tuples.
    for j in range(1, len(Y)-k+1):
        hash_value_y = (d*(hash_value_y - ord(Y[j-1])*h) + ord(Y[j+k-1])) % q
        if h_table_x[hash_value_y % table_size]:
            for word in h_table_x[hash_value_y % table_size]:
                if word[0] == Y[j:j+k]:
                    tuples.append((word[1], j))  
    return tuples
    
    
    
    
    
    # Test 1: Two strings with common substrings
#Result: Return correct index.
x = "todayismonday"
y = "day"
k = 3
assert rh_get_match(x, y, k) == [(2, 0), (10, 0)]

#Test 2: Two strings with common strings and numeric numbers
#Return correct index.
n ="ababacccc134"
m ="a134"
t=3
assert rh_get_match(n, m, t) == [(9, 1)]
# Test 3: Two strings with no common substring 
# Result: Empty list 
h = "todayismonday"
z = "zxlp"
l = 3
assert rh_get_match(h, z, l) == []


#Part 2:
#the function is
def hash_function(string):
    value = 0
    for char in string:
        value = value*127+ord(char)
    return value
def rh_get_match(X, Y, k):
    # stores list of tuples containing positions of common substrings
    #use tuples because 
    tuples_list = []
    # necessary parameters
    # length of strings X and Y
    n_x = len(X)
    n_y = len(Y)
    
    # values to store rolling hash values for substrings of X and Y
    hash_value_x = 0
    hash_value_y = 0
    
    # hash table to store substrings and their indexes
    # I ensure that the table is at most 60% full
    table_size = int(n_x-k+1) 
   
    #create a 2D table
    h_table_x = [[] for i in range(table_size)]
    
    #for loop for calculating the value of consecutive substring
    #and append the substring into the hash table
    #checking for substring for the first string X
    #the for loop use range of n_x-k+1- the total number of substring length k we have
    #For instance, we have 5 items =[a,b,c,d,e].
    #the number of substring length 3 we have is:
    #[a,b,c],[b,c,d],[c,d,e].
    #Therefore, the total number of substrings k is n_x - k+1.
    for i in range(n_x-k+1):
        #substring based on the the value of i
        sub = X[i:i+k]
        #calculate the value of substring-k by using 
        #helper function hash_function
        hash_value_x = hash_function(sub)
        #append the sub_string length k and i into the hash_table
        #by using its hash_value
        h_table_x[hash_value_x % table_size].append((sub, i))
    
    #checking the substring of second string Y.
    for j in range(n_y-k+1):
        #substring based on the the value of j
        sub = Y[j:j+k]
        #calculate the value of substring-k by using 
        #helper function hash_function
        hash_value_y = hash_function(sub)
        #check if the list with index based on the value of substring from second string Y
        # is not empty, which means substring-lenth-k from string 1 (X)
        #has the same hash_value as the substring_length_k from string 2(Y)
        if h_table_x[hash_value_y % table_size]:
            for word in h_table_x[hash_value_y % table_size]:
        #check whether any item in the list would equals 
        #the substring_length_k from second string Y.
                if word[0] == Y[j:j+k]:
                    #append the substring into the tuple and store j
                    tuples_list.append((word[1], j))
    return tuples_list




#Part 3:
#function used to calculate the hash value for string
def hash_function(string):
    value = 0
    for char in string:
        value = value*127+ord(char)
    return value
import string 
import random
#function randomword to create different random words
def randomword(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
#define table size
table_size = 5000
#create hash_tab by using comprehension loop
hash_tab = [[] for i in range(table_size)]
#based on the previous function randomword, create word_bank that each word with length of 10
word_bank = [randomword(10) for i in range(5000)]
#append each word into the hash_table
for word in word_bank:
    hash_tab[hash_function(word) % table_size].append(word)
#the number of collisions.
collisions = 0
#sum of collisions
sum_collisions = 0
for list_ in hash_tab:
    #if the list is not empty and list has more than 1 items
    #meaning that the list has collisions
    if list_ and len(list_) > 1:
        collisions += 1
        sum_collisions += len(list_)

print(collisions/len(hash_tab))
print(sum_collisions/collisions)
