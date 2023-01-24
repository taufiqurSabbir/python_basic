language_list= ['python','Javascript','java','php','go']


while True:
    task = input('Input what do you want? read/create/update/delete: ')
#read list
    if task=='read':
        print('language',language_list)

#Insert new item to list
    elif task =='create':
        pos=int(input('Enter position of insert:'))
        if pos <= len(language_list)+1:
            value = input('Enter The value:')
            language_list.insert((pos-1),value)
            print('language', language_list)
        else:
            print('Trying to insert in wrong position')
 #Update item
    elif task=='update':
        print('language', language_list)
        pos = int(input('Enter position of Update:'))
        if  pos <= len(language_list):
            value = input('Enter The value:')
            language_list[pos-1]=value
            print('language', language_list)
        else:
            print('Trying to update in wrong position')
#delete item
    elif task=='delete':
        con =input('delete with position or value?')
        if con=='position':
            pos = int(input('Enter position of Delete:'))
            if pos <= len(language_list):
                language_list.pop(pos-1)
                print('language', language_list)
            else:
                print('Wrong Position')
        elif(con=='value'):
            pos = (input('Enter value of Delete:'))
            language_list.remove(pos)
            print('language', language_list)
        else:
            print('Wrong position or value not in list')
