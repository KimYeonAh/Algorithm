NO_OF_CHARS = 128

def shift_table(pat) :
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1) :
        tbl[ord(pat[i])] = m-1-i
    
    return tbl

def search_horspool(T,P) :
    patLen = len(P)
    textLen = len(T)
    table = shift_table(P)
    patHigh = patLen-1

    while patHigh <= textLen - 1 :
        matCount = 0
        while matCount <= patLen -1 and P[patLen-1-matCount] == T[patHigh-matCount] :
            matCount += 1
        
        if matCount == patLen :
            return patHigh - patLen + 1
        else :
            patHigh += table[ord(T[patHigh])]
    
    return -1
