# Generate Binary Numbers  -----------------------------------

def generate(N):
    res = []
    for i in range(1,N+1):
        res.append(bin(i).replace("0b",""))
    return res