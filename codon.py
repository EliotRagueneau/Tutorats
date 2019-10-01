


def codon(seq):
    a=0
    truc=0
    for i in range(len(seq)):
        if seq[i:i+3]=="ATG":
            a=i+3
            for o in range(a,len(seq),3):
                if seq[o:o+3]=='TAA'or seq[o:o+3]=='TAG'or seq[o:o+3]=='TGA':
                    count=count+1
    if count!=0 :
        return True

    else:
        return False




seq='CTGATGTTCCAATAACCAGAA'
num = codon(seq) # 3
print(num)
