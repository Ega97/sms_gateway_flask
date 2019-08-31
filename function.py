
no = 1
for x in no:
rec=0 
def autoIncrement(): 
    global rec 
    pStart = 1    #adjust start value, if req'd   
    pInterval = 1 #adjust interval value, if req'd 
    if (rec == 0):   
        rec = pStart   
    else:   
        rec = rec + pInterval   
    print(rec)
    return rec
if __name__ == "__main__":
    autoIncrement()