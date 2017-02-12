# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:29:30 2017

@author: sukrit
"""

text = """As long as your only concern is placing text on a Web page, it makes no difference
whether your page is about music or mushrooms. However, if Richard wants to implement
a search engine that can quickly scan this document and extract information about
the artist or music tracks, it would help if the document structure told the search engine
something about the document content. Without being able to determine whether a particular
tag refers to the title, music track, price, or artist, it’s difficult to locate the precise
piece of information that Richard might want."""



# remove all punctuation marks and convert to lower case
my_str = text.replace(".","").replace(",","").replace("’","").lower()
print(my_str)
stop_words = ["a","the","an","if","is","are","as","of","it","on","to","or","and"]
ss = my_str.split()
print(len(stop_words))
print(ss[1])

b=[]
for i in range(len(ss)):
    count = 0
    for j in range(len(stop_words)):
        if ss[i] == stop_words[j] :
            count += 1         
    if count == 0:
        a=ss[i]    
        b.append(a)    

print(" ".join(b))        

   # matrix = [[randint(1,100) for i in range(10)]for i in range(4)]
# remove the stop-words (frequently appearing words)

# count how many times each word occurs in the text