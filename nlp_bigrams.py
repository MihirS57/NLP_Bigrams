import nltk
from nltk import word_tokenize

corpus = "eos I really appreciate your help eos I is really sorry for not inviting you eos I really like your watch eos"
corpus_ex = "eos You book a flight eos I read a book eos You read eos"
val = 1
dic = {}

curr_corp = corpus_ex
curr_corp = curr_corp.lower()
tokens = word_tokenize(curr_corp)
pure_tokens = list(dict.fromkeys(tokens))

def getProbs(id=-1,tokens=[],corp="",token_p="",token_c=""):
    if id != -1:
        prev = tokens[id-1]
        curr = tokens[id]
        num = prev+" "+curr
    else:
        num = token_p+" "+token_c
        if len(token_p) == 1:
            token_p = " "+token_p+" "
        prev = token_p
    if num not in dic:
        n_num = corp.count(num)
        n_prev = corp.count(prev)
        prob = n_num/n_prev
        dic[num] = prob
    #print(f'P({num}|{prev}) => {dic[num]}')
    return dic[num]


print(f'Calculating probabilities w.r.t: {curr_corp}')
for token_i in pure_tokens:
    for token_l in pure_tokens:
        getProbs(corp=curr_corp,token_p=token_i,token_c=token_l)

print("Bigram Table: ")
print("       ",*pure_tokens,sep="\t")
for token_1 in pure_tokens:
    print(token_1,end="\t")
    for idx,token_2 in enumerate(pure_tokens):
        if idx != len(pure_tokens)-1 :
            print(dic[token_1+" "+token_2],end="\t")
        else:
            print(dic[token_1+" "+token_2])
    
curr_corp = "eos you read a book eos"
curr_corp = curr_corp.lower()
print(f'Now testing it for a sentence: {curr_corp}')
tokens = word_tokenize(curr_corp)
for i in range(1,len(tokens)):
    prob = getProbs(id=i,tokens=tokens,corp=curr_corp)
    val = val*prob
    num = tokens[i-1]+" "+tokens[i]
    prev = tokens[i-1]
    print(f'P({num}|{prev}) => {prob}')
print(val)

    
    



