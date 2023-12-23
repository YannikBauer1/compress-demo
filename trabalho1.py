import math
import bitstring




def compressor(bitString):
    S=["lambda", bitString[0]]
    output=bitString[0]
    bitString=bitString[1:len(bitString)]
    while len(bitString)!=0:
        i = nextComp(S,bitString)
        if i==0:
            nextS="0"+bitString[0]
            output = output + nextS
            S = S + [bitString[0]]
            bitString=bitString[1:len(bitString)]
        else:
            print(S)
            print(i)
            print(bitString)
            nextS=S[i]+bitString[len(S[i])]
            numBit=math.ceil(math.log(len(S),2))
            output = output + get_bin(i,numBit) + bitString[len(S[i])]
            S = S + [nextS]
            bitString=bitString[len(S[i])+1:len(bitString)]
        #print(output)
    return output

get_bin = lambda x, n: format(x, 'b').zfill(n)
def nextComp(S,bitString):
    for i in range(len(S)-1,0,-1):
        if S[i]==bitString:
            continue
        elif S[i]==bitString[0:len(S[i])]:
            return i
    return 0
def remove(bitstring,n):
    l=len(bitstring)
    if n<1 or n>l:
        return "n out of Range"
    else:
        return bitstring[0:n-1]+bitstring[n:l]
def give(bitstring,n):
    l = len(bitstring)
    if n < 1 or n > l:
        return "n out of Range"
    else:
        return bitstring[n-1]

#print(compressor("10110011111111111111"))

def decompressor(input):
    output=input[0]
    S = ["lambda", input[0]]
    input=input[1:len(input)]
    while len(input)!=0:
        print(S)
        print(input)
        i=get(S,input)
        if i==0:
            output=output+input[0]
            S=S+[input[0]]
            input=input[2:len(input)]
        else:
            print(i)
            numBit = math.ceil(math.log(len(S), 2))
            bit = get_bin(i, numBit)
            output=output+S[i]+input[len(bit)]
            print("asdfasdf",input[len(bit)])
            S=S+[S[i]+input[len(bit)]]
            input=input[len(bit)+1:len(input)]
    return output

def get(S,input):
    for i in range(len(S)-1,-1,-1):
        numBit = math.ceil(math.log(len(S), 2))
        bit=get_bin(i,numBit)
        if bit==input:
            continue
        elif bit==input[0:len(bit)]:
            return i

print(decompressor(compressor("10110011111111111111")))