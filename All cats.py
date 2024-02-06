catNames = [] 
while True:
    print("Вкажіть ім'я кота або кошки " + str(len(catNames) + 1) + " (<Enter> для завершения):")
    name = input() 
    if name == '':
        break
    catNames = catNames + [name] #конкатенация списков
print("Імʼя котів та кішок:") 
for name in catNames:
    print(' ' + name)