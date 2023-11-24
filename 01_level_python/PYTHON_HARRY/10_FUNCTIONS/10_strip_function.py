def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this="    HARRY IS GOOD   "
n=remove_and_strip(this,"HARRY")
print(n)