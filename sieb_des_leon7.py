def sieb_des_leon7(n):                      
    if n < 2:                               
        return []
    is_prime = [2]
    uneven_index_from3 = [True] * ((n-1)//2)
    
    for uneven_index_candidate in range(0,int(n**0.5)//2):
        if not uneven_index_from3[uneven_index_candidate]:
            continue
    
        uneven_candidate = uneven_index_candidate*2+3
        is_prime.append(uneven_candidate)
    
        for false in range((uneven_candidate)**2//2-1,len(uneven_index_from3),uneven_candidate):
            uneven_index_from3[false] = False

    for primeaftersqroot in range(int(n**0.5)//2,(n+1)//2-1): #nachbearbeiten für alle zahlen nach n**0.5
        if uneven_index_from3[primeaftersqroot]:
            is_prime.append(primeaftersqroot*2+3)
        
    return is_prime

print(sieb_des_leon7(120))