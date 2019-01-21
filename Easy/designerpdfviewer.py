#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
h=[1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,7]
word='zaba'
import string

def designerPdfViewer(h, word):
    letters=path=list(map(str, word))
    order=[]
    h_result=[]
    for l in letters:
        order.append(string.ascii_lowercase.index(l))
    for o in order:
        h_result.append(h[o])


    return max(h_result)*len(word)

print( designerPdfViewer(h, word))
