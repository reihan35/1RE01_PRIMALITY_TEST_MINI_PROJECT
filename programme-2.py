def modulo(a,n,p):
    """cette fonction calcule a à la puissance n modulo p sans calculer a à la
    puissance p."""
    k=1
    i=0
    #On commence par n=1 jusqu'a n et à chaque tour de boucle on calcule a à la puissance n  modulo p et on retourne le résultat final"
    
    while i<n:
        k=(k*a)%p
        i=i+1
    return k

assert(modulo(2,15,100)==68)
assert(modulo(5,15,3)==2)
assert(modulo(6,80,52)==16)
