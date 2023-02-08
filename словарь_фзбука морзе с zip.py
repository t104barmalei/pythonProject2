letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']
a=dict(zip(letters,morse))
# print(a)
b=input()
c=''
for i in range(len(b)):
    for key,value in a.items():
        if b[i].upper() ==key:
          c+=value+' '
print(c.rstrip())



