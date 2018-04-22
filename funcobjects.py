def fun1(text):
    return text.upper()
print(fun1("python"))
assg=fun1("mint")
print(assg)

def fststd(text):
    return text.upper()
def secondstd(text):
    return text.lower()
def mastercls(func):
    outfuc=func("Hello This is python Learning")
    print outfuc

mastercls(fststd)
mastercls(secondstd)