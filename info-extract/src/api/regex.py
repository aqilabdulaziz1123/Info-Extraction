import re

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"

def getdigits(text,keyword):
    s = text.split(' ')
    for i in range(len(s)):
        s[i] = re.sub(digits + "[.]" + digits, '\\1\\2',s[i])
        s[i] = re.sub(digits + "[,]" + digits, '\\1\\2',s[i])
    pos = [i for i,st in enumerate(s) if keyword in st]
    if pos:
        posi = pos[0]
    else:
        posi = None
    return [(int(st),i)for i,st in enumerate(s) if st.isdigit()],posi
    # return re.findall('\\b\\d+\\b', text)
    
def getclosest(arr,pos):
    cl = arr[0]
    for i in arr:
        if abs(i[1] - pos) < abs(cl[1] - pos):
            cl = i
    return cl


# def gettanggal(text):

    


def split(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    text = re.sub(digits +  "+[.]" + digits+"+","\\1<prd>\\2",text)
    if "”" in text:
        text = text.replace(".”","”.")
    if "\"" in text:
        text = text.replace(".\"","\".")
    if "!" in text: 
        text = text.replace("!\"","\"!")
    if "?" in text: 
        text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


def splittxt(dir,filename):
    with open(dir+'/' +filename,'r') as f:
        text = f.read()
        # print(text)
    sentences = split(text)
    # print(sentences)
    return sentences