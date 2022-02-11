from nltk.tag import pos_tag
import re

def spanbio(sent, toks):
    """
    Format:
    sent - Sentence - Simple String
    toks - Spans as Dictionary - Ex. {'start': [0, 13, 22], 'end': [4, 19, 27]}
    """
    samplespanstart = toks['start']
    samplespanend = toks['end'].copy()
    print("preadd", samplespanstart,samplespanend)
    for i in range(len(samplespanend)):
        samplespanend[i] = samplespanend[i] + 1
    ls = ['O']*len(sent.split())
    print(sent.split())
    print("lslen", len(ls))
    for i, j in zip(samplespanstart,samplespanend):
        print(i,j)
        for k in range(i,j):
            ls[k] = 'B'
    for i in range(1,len(ls)):
        if (ls[i-1] == 'B' and ls[i] == 'B'):
            ls[i] = 'I'
        elif (ls[i-1] == 'I' and ls[i] == 'B'):
            ls[i] = 'I'
    return ' '.join(ls)

def get_numeric_spans(tofind_spans, full_sent):
    """
    Format:
    tofind_spans: Spans of Text corresponding to the sentence - Ex. [I like to play, he likes to run]
    full_sent: Sentence as String - Ex. I like to play soccer while he likes to run
    """
    dict_spans = {}
    dict_spans['start'] = []
    dict_spans['end'] = []
    ls_joined = []
    for i in tofind_spans:
        ls_joined.append(i)
    ls_joined_no_repeats = []
    for i in ls_joined:
        if (i not in ls_joined_no_repeats):
            ls_joined_no_repeats.append(i)
    for i in ls_joined_no_repeats:
        for match in re.finditer(i, full_sent):
                start = match.start()
                end = match.end()
                words_before = full_sent[:start].count(' ')
                words_inmidst = i.count(' ')
                dict_spans['start'].append(words_before)
                dict_spans['end'].append(words_before+words_inmidst)
    dict_spans['start'].sort()
    dict_spans['end'].sort()
    return dict_spans

def postagsget(sent):
    """
    sent: Sentence as string
    """
    string = ""
    ls = pos_tag(list(sent.split()))
    for i in ls:
        string += i[1] + " "
    return string

if __name__ == "__main__":
    sent = "I like to play soccer while he likes to run"
    toks = {'start': [0, 6], 'end': [3, 9]}
    print(spanbio(sent, toks))
    tofind_spans = ["I like to play", "he likes to run"]
    full_sent = "I like to play soccer while he likes to run"
    print(get_numeric_spans(tofind_spans, full_sent))
    print(postagsget(sent))
