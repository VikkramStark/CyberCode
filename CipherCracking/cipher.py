import enchant 
dic = enchant.Dict("en_us") 

def RotateCipher(text, value): 
    text = text.lower() 
    num_values = range(26) 
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]

    num_str = dict(zip(num_values, alpha)) 
    str_num = dict(zip(alpha, num_values)) 

    res = '' 
    for c in text:
        if c.isalpha():
            res+=num_str[((str_num[c]+value)%26)] 
        else:
            res += c

    return res 


for i in range(26):
    rotated_words = RotateCipher("KROKN SXTOMD EXPYVN OKCSVI",i)
    words = rotated_words.split() 
    for word in words:
        if dic.check(word): 
            print(rotated_words,i) 
            break   
