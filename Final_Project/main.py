from rpg import Mage,Knight

knight =Knight("Арториас",100,40,50)
mage = Mage("Артес",100, 90, 30)

herous =[knight,mage]
print("початок битви")
print(knight)
print(mage)

while True:
    knight.attack(mage)
    mage.attack(knight)
