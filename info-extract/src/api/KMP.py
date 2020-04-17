import os
from regex import splittxt, getdigits, getclosest
from copy import deepcopy

txtdir = "../../../txtfiles"

def lps(pat):
    ar = [0 for i in pat]
    for i in range(len(ar)):
        stop = False
        for j in range(i+1,len(ar)):
            if pat[i] == pat[j] and ar[j-1] == i:
                stop = True
                ar[j] = 1 + ar[j-1]
                # print(i,j)
        if not stop:
                break
    return ar

def knp(st,pat):
    lp = lps(pat)
    i = 0
    j = 0
    pos = []
    while ( i < len(st)):
        if st[i] == pat[j]:
            i += 1
            j += 1
        elif st[i] != pat[j]:
            if j == 0:
                i+=1
            else:
                j = lp[j-1]
            
        if j == len(pat):
            # print(i-len(pat))
            pos.append(i-len(pat))
            break
            # count += 1
            j = 0
    return pos

def solve(dir,pat):
    files = []
    for filename in os.listdir(dir):
        files.append(filename)
    
    for filename in files:
        sentences = splittxt(dir,filename)
        for i in range(len(sentences)):
            x = knp(sentences[i],pat)
            y,p = getdigits(sentences[i],pat)
            # print(y,p)
            if p:
                print(getclosest(y,p))
            if not x:
                pass
            else:
                print(filename)
                # print(i)
                print(x[0])
# print(knp("halo, sya adalah 5000.0000 orang. ada 293 orang meninggal.","meninggal"))
# solve('tes','meninggal')

def solvemany(list,key):
    lshasil = []
    hasil = {}
    no = 0
    # bentuk hasil [namafile,kalimat]
    for filename in (list):
        sentences = splittxt(txtdir,filename)
        for i in range(len(sentences)):
            x = knp(sentences[i].lower(),key.lower())
            y,p = getdigits(sentences[i],key.lower())
            if p:
                # print(getclosest(y,p)[0])
                hasil['digit'] = getclosest(y,p)[0]
            if x:
                # print(filename)
                hasil['nama'] = filename
                # print(x[0])
                # print(sentences[i])
                hasil['kalimat'] = sentences[i]
                hasil['id'] = no
                no+= 1
                lshasil.append(deepcopy(hasil))
        hasil.clear()
    print(lshasil)
    return lshasil
        
                


# ls = ['a','b','c']
# solvemany(ls,'meninggal')