#course1 
#week1
#------------------------------------------------------------------
def patterncount(text,pattern):
    count = 0
    for i in range(0,len(text) - len(pattern)+1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count
	
	
	
#---------------------------------order ~ O(|text|^2	*k) --- bad running time- need to improve)
def frequentwords(text,k):
    freq_pat = []
    count = []
    for i in range(0,len(text) - k):
        pattern = text[i:i+k]
        #print (pattern)
        #print (patterncount(text,pattern))
        count.insert(i,patterncount(text,pattern))
    maxCount = max(count)
    for j in range(0, len(text) - k):
        if count[j] == maxCount:
            freq_pat.append(text[j:j+k])
    print (freq_pat)
    unique = set(freq_pat)
    return(unique)


#----------------------------------------------------- reverse complimentary-----

def reverse_complement(text):
	code = str.maketrans("ATGC", "TACG")
    return text.translate(code)[::-1]
---------------------------------------------------------------------------------
   
