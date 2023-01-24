time = {1,2,5,9,7,6}
work = {10,50,2,9,20}
#print single element
for x in time:
    print(x)

#add in set

time.add(99)
print(time)

#delete item

time.discard(7)
print(time)

#union of 2 set

print(time | work)

#set intersection
print(time & work)
# delete full set

del time