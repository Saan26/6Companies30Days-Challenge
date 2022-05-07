# Run Length Encoding --------------------------------
def encode(str_):
    res = ''
    str_ += '#'
    c = 1
    for i in range(len(str_) - 1):
        if str_[i] == str_[i+1]:
            c += 1
            continue
        else:
            res += str_[i] + str(c)
            c = 1
            
    return res
