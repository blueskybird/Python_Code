# -*- coding: utf-8 -*-

def reduce_dim():
    synonym_items=[]
    all_word=[]
    
    synonym_path=r'C:\Users\Administrator\Desktop\hagongdaSynonym.txt'
    vec_path=r'C:\Users\Administrator\Desktop\wordCount.txt'
    f=open(synonym_path,'r')
    content=f.readline()
    while content:
        synonym_items.append(content.split(' ').strip())
        content=f.readline()
    f.close()
    
    f=open(vec_path,'r')
    word=f.readline()
    while word:
        all_word.append(word.strip())
        word=f.readline()
    
    for item in synonym_items:
        if str in item:
            print item[0]
            

if __name__=='__main__':
    str=['你','你好','好','你','门']
    str=list(set(str))
    print str