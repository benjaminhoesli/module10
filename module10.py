import sys
x=sys.argv

def encrypt(n):
    inp=input("enter message")
    inp=inp.upper()
    final=""
    block = ""
    count=0
    for ch in inp:
        if ch in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            count+=1
            ordi=ord(ch)+n
            if ordi<=90:
                block+=(chr(ordi))
            else:
                block+=(chr(ordi-26))
            if len(block)>4:
                final+=(block)
                final+=" "
                count+=1
                block=""
        if count==59:
            final+='\n'
            count=0
    if len(block)>0:
        if count+len(block)<59:
            final+=block
        else:
            final+='\n'
            final+=block
    return final


print(encrypt(int(x[1])))
