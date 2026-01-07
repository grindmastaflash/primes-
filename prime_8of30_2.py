"""8 possible positions relative to multiples of 30 are possible prime position, with exeption of 3,5 and NOT 1
so primes30[0]: 0-29,primes30[1]: 30-59,primes30[2]: 60-89,...
+1,+7,+11,+13,+17,+19,+23,+29 for bit index 0-7 in byte
"""


def prime_8of30_2(n):
    n_by_30 = n//30 + 1
    deltafrom_30s = [1,7,11,13,17,19,23,29]
    is_prime = [2,3,5]
    primes30 = bytearray([255]*n_by_30)

    primes30[0] &= ~(1 << 0)            # set bit for decimal 1 to 0 

    for block_index, byte in enumerate(primes30):   #iterate over every byte
        for bit in range(8):                        #iterate over every bit per byte
            if primes30[block_index] & (1 << bit):                    #if bit == 1: number represented by bit is prime 
                prime = 30* block_index + deltafrom_30s[bit]
                is_prime.append(prime)
                not_block,not_delta_from = divmod(prime**2, 30)

                while not_block < n_by_30:          #maybe <=   
                    
                    if not_delta_from in deltafrom_30s:   #set multiples of prime to zero in its bit represantation
                        primes30[not_block] &= ~ (1<<deltafrom_30s.index(not_delta_from))

                    nextcheck = 2* prime+ not_delta_from
                    not_block += nextcheck // 30
                    not_delta_from = nextcheck % 30


    return is_prime


print(prime_8of30_2(119))