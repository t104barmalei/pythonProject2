pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in range(len(pets)):
    result.setdefault(pets[i][1:],[pets[i][0]])
    if pets[i][0] not in result.get(pets[i][1:]):
        result.get(pets[i][1:]).append(pets[i][0])
print(result)
# варианты условия
# if pets[i][0] not in result.get(pets[i][1:]):
#     result.get(pets[i][1:]).append(pets[i][0])

# if pets[i][0] not in result[pets[i][1:]]:
#     result[pets[i][1:]].append(pets[i][0])

# if pets[i][0] not in result.get(pets[i][1:]):
#     result[pets[i][1:]].append(pets[i][0])
