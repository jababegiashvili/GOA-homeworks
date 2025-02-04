def filter_list(l):
    return [character for character in l if type(character)!= str]



def solution(text, ending):
    len_ending=len(ending)
    if len_ending > len(text):
        return 0
    last_word_of_text = text[len (text)- len_ending:]
    return   last_word_of_text == ending



def get_middle(s):
    if len(s) % 2 == 0:
        start = int (len(s)*.5)-1
        end = int(len(s)*.5)+ 1
        return s[start:end]
    
    return s[int(s*.5)]
