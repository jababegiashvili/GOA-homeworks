def xo(s):
    return s.lower().count('x')==s.lower().count('o')



def find_short(s):
    words = s.split(' ')
    words.sort(key=len)
    return len(words[0])