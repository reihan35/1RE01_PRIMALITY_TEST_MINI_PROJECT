def fonc2(a,n):
    """int->int
    calcul a^(n-1)% n sans calculer a^(n-1)  """
    k=1
    i=0

    while i<n-1:
         k=(k*a)%n
         i=i+1
    return k

def fonc3(a,n,p):
    """int->int
    calcul a^(n-1)% n sans calculer  a^((n-1)/p)%n"""
    k=1
    i=0

    while (i<(n-1)//p):
        k=(k*a)%n
        i=i+1
    return k

def pgcd(a,b):
    """int->int
    pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
     
def reciproqueFermat(n):
    """int->bool
    la réciproque de theroem de Fermat nous dit que l'entier n est premier si:
    si il existe un a appartenant à premier à n tel que on a:
    a^(n-1)%n =1 et a^((n-1)/p)%n!=1 ∀ p telque (n-1)%p=0
    la fonction renvoit True si le nombre est premier ,False si non."""

    m=0
    s=0
    g=0
    L=[]
    x=0
    M=[]
    e=1

    if n==1:
         return False
    elif n%2==0 and n!=2:
        return False
    elif n==2:
        return True

    else:
        while e<n:             #On construit l'ensemble M contenant tous les a telque a est premier à n.
            if pgcd(e,n)==1:
                M.append(e)
            e=e+1

        for x in range (2,n):  #On construit l'ensemble L contenant tous les p telque (n-1)%p=0.
            if n-1%x==0:
                L.append(x)
    
    
        while s<len(L) :       #On verifie la premeir condition si c'est le cas on verifie la suite si non on renvoit False.
            while g<len(M):
                if fonc3(M[g],n,L[s])!=1:
                    g=g+1
                    s=s+1
                else:
                    return False
        g=0
        while g<len(M):        #On verifie la deuxiem condition on revoit True si c'est le cas ,False si non.
            if fonc2(M[g],n)==1:
                g=g+1
            else:
                return False
            
        

    return True
    
assert(reciproqueFermat(22)==False)
assert(reciproqueFermat(27)==False)
assert(reciproqueFermat(561)==True)
