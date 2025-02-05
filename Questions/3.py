import collections
path="poem.txt"
with open(path,"r") as f :
    content=f.read()
    l=content.split()
    print(l)
    word_count=collections.Counter(l)
    m_word=max(word_count,key=word_count.get)
    m_count=word_count[m_word]
    print(f"{m_word}= {m_count} times ")


    