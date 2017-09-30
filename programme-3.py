#Programme de décomposition en facteur premier
import math
def estpremier(n):
    """
    int->bool
    estpremier(n): dit si un nombre est premier (renvoie True ou False) en
    utilisan le faite que :Si n est un nombre composé alors il a au moins un
    un diviseur inférieur à racine de n."""
    if n<7:
        if n in (2,3,5):
            return True
        else:
            return False
    # si n est pair et >2 (=2: cas traité ci-dessus),il ne peut pas être premier
    if n & 1 == 0:
        return False
    # autres cas
    k=3
    r=math.sqrt(n)
    while k<=r:
        if n % k == 0:
            return False
        k+=2
    return True
 
assert(estpremier(5)==True)
assert(estpremier(38)==False)

def facteurpremier(n):
    """int->liste[int]
       renvoi la liste des facteurs premierd de n."""

    s=2
    L=[]

    if estpremier(n)==True:   
        return n

    else:
        for s in range (2,n+1):
            if n%s==0:
                if estpremier(s)==True:
                    L.append(s)
    return L

assert (facteurpremier(120)==[2, 3, 5])
assert (facteurpremier(2305)==[5, 461])
assert (facteurpremier(13)==13)
