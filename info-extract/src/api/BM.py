def badH(pattern):
    dic = {}
    for i in range(len(pattern)):
        dic[pattern[i]] = i
    return dic


def badHS(txt,pat):
    m = len(pat) 
    n = len(txt) 
  
    # create the bad character list by calling  
    # the preprocessing function badCharHeuristic() 
    # for given pattern 
    badChar = badH(pat)  
  
    # s is shift of the pattern with respect to text 
    s = 0
    while(s <= n-m): 
        j = m-1
  
        # Keep reducing index j of pattern while  
        # characters of pattern and text are matching 
        # at this shift s 
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
  
        # If the pattern is present at current shift,  
        # then index j will become -1 after the above loop 
        if j<0: 
            print("Pattern occur at shift = {}".format(s)) 
            s += (m-badChar[txt[s+m]] if s+m<n else 1) 
        else: 
            s += max(1, j-badChar[txt[s+j]]) 


badHS("ABABAAABAABAAAA","ABA")