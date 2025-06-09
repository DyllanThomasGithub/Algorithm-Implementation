# Dyllan Thomas, Myles David
# Python implementation of stable matching problem
# Project 1 Code
# CS 2123 last modified 9/11/19

def gs(men, women, pref):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank={}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m]=i
            i+=1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)    #initially all men and women are free
    numpartners = len(men) 
    S = {}           #build dictionary to store engagements 

    #run the algorithm
    while freemen:
        m = freemen.pop()
        #get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m]+=1
        if w not in S: S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

def gs_block(men, women, pref, blocked):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank = {}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
                rank[w][m] = i
                i += 1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)  # initially all men and women are free
    numpartners = len(men)
    S = {}  # build dictionary to store engagements

    # run the algorithm
    while freemen:
        m = freemen.pop()
        # get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m] += 1
        if prefptr[m] >= numpartners:
            print(m + " has no partner")
            break
        elif w not in S:
            if (m, w) not in blocked:
                S[w] = m
            else:
                freemen.add(m)

        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime] and (m, w) not in blocked:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

def gs_tie(men, women, preftie):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of sets of preferred names in sorted order)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank = {}
    for w in women:
        rank[w] = {}
        i = 1
        for m in preftie[w]:
            for val in m:
                rank[w][val]=i
            i += 1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)  # initially all men and women are free
    numpartners = len(men)
    S = {}  # build dictionary to store engagements

    # run the algorithm
    while freemen:
        m = freemen.pop()
        val = prefptr[m]
        # get the highest ranked woman that has not yet been proposed to
        hSet = preftie[m][prefptr[m]]
        w = next(iter(hSet))
        prefptr[m] += 1
        if w not in S:
            S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S

if __name__=="__main__":
    #input data
    themen = ['xavier','yancey','zeus']
    thewomen = ['amy','bertha','clare']

    thepref = {'xavier': ['amy','bertha','clare'],
           'yancey': ['bertha','amy','clare'],
           'zeus': ['amy','bertha','clare'],
           'amy': ['yancey','xavier','zeus'],
           'bertha': ['xavier','yancey','zeus'],
           'clare': ['xavier','yancey','zeus']
           }
    thepreftie = {'xavier': [{'bertha'},{'amy'},{'clare'}],
           'yancey': [{'amy','bertha'},{'clare'}],
           'zeus': [{'amy'},{'bertha','clare'}],
           'amy': [{'zeus','xavier','yancey'}],
           'bertha': [{'zeus'},{'xavier'},{'yancey'},],
           'clare': [{'xavier','yancey'},{'zeus'}]
           }
    
    blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}

    #eng
    match = gs(themen,thewomen,thepref)
    print(match)
    
    match_block = gs_block(themen,thewomen,thepref,blocked)
    print(match_block)

    match_tie = gs_tie(themen,thewomen,thepreftie)
    print(match_tie)
