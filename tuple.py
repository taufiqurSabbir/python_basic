lang = ('php','python','java','go','rust')

cd = list(lang)

cd.append('flutter')
cd.insert(1,'javascript')
cd.remove('go')
lang = tuple(cd)
print(lang)