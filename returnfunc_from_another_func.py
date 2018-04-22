def func1(x):
    def func2(y):
        return x**y
    return func2
outfunc=func1(1)
print(outfunc(12))

def myfun(word):
    let=''
    word=word.lower()
    for i in range(len(word)):
        if i % 2 ==0:
            let+=word[i].upper()
        else:
            let+=word[i].lower()
    return let
print(myfun("python"))
