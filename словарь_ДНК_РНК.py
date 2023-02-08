DNK_RNK={'G':'C','C':'G','T':'A','A':'U'}
a=input()
RNK=''
for i in a:
    RNK+=DNK_RNK[i]
print(RNK)