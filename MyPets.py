
myPets = ['Софи', 'Питер', 'Толстяк'] 
print("Вкажіть ім'я кота або кошки:") 
name = input()
if name not in myPets:
    print("У мене немає домашнього улюбленця по імені " + name) 
else:
    print(name + ' - мой питомец.')
