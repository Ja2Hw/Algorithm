def solution(numer1, denom1, numer2, denom2):
    n = numer1 * denom2 + numer2 * denom1
    d = denom1 * denom2
    if n > d:
        k = d
    else:
        k = n
    i = 2
    while i <= k : 
        if n % i == 0 and d % i == 0:
            n /= i
            d /= i
            if n > d:
                k = d
            else:
                k = n
            i = 1
        i += 1
    return [n,d]