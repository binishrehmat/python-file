#add list items
#append()
subjectlist=["ai","cn","ds"]
subjectlist.append ("calculus")
print (subjectlist)
#insert()
subjectlist=["ai","cn","ds"]
subjectlist.insert (2,"calculus")
print (subjectlist)
#extend()
subjectlist=["ai","cn","ds"]
subjectmarks=[29,28,26]
subjectlist.extend (subjectmarks)
print(subjectlist)



#remove list items
#remove
subjectlist=["ai","cn","ds"]
subjectlist.remove ("cn")
print (subjectlist)
#pop
subjectlist=["ai","cn","ds"]
subjectlist.pop (2)
print (subjectlist)
#delete
subjectlist=["ai","cn","ds"]
del subjectlist [1]
print (subjectlist)
#remove
subjectlist=["ai","cn","ds"]
subjectlist.clear ()
print (subjectlist)