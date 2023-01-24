dict = {'php':500,'python':700,'java':1000,'go':900}

print(dict['php'])

#print key

print(dict.keys())

#print value
print(dict.values())

#value with get

x=dict.get('java')
print(x)


#add
dict['javascript'] = 800

print(dict)

#update

dict.update({'go':500})

print(dict)

#remove
dict.pop('java')
print(dict)