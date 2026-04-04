asc = []
def sort(value):
    print("in sort value 1")
    i = 0
    j = len(asc)
    if len(asc) == 0:
       print("in if")
       asc.append(value)
       print("after append 0")
       print("asc = ", asc)
    
    else:
        print("in else")
        while i<j:
            print("in while")
            if asc[i]>value>asc[j-1] and i!=(j-1) and value not in asc:
                print("in between")
                i=i
                j=j
                print("incremented")
                print("asc = ", asc, "i = ",i, "j = ",j)

            elif value > asc[i] and value not in asc:
                print("in while if")
                asc.insert(i, value)
                print("after while if")
                print("asc = ", asc)
            
            elif value < asc[j-1] and value not in asc:
                print("in while elif 1")
                asc.insert(j, value)
                print("after while elif 1")
                print("asc = ", asc, "i = ", i, "j = ", j)   

            i=i+1
            j=j-1  

        return 

def top_n(name, count):
    unsorted = []
    for key in name:
        #print(name[key])
        unsorted.append(name[key])
    
    for i in unsorted:
        sort(i)
    
    print("sorted all")
    top_count = []
    k=0
    while k < count:
         top_count.append(asc[k])
         k = k+1
    keys = []
    for i in top_count:
        key = [k for k, v in name.items() if v == i]
        keys.append(key[0])
    print(keys)

        




error_counts = {
    "TimeoutError": 45,
    "ConnectionRefused": 12,
    "OOMKilled": 78,
    "CrashLoopBackOff": 34,
    "ImagePullBackOff": 5
}

top_n(error_counts, 3)