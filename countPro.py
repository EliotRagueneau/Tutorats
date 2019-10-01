


def countPro(seq,x):
    a=0
    for i in range(len(seq)):
        if seq[i]==x :
            a=a+1
    return a




seq='MVHLSAEEKEAVLGLWGKVNVDEVGGEALGRLLVVYPWTQ'
num = countPro(seq,"M") # The correct answer is 1
print(num)
