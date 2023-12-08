def selsort(a): 
    l = len(a)
    for i in range(l):
        m = i
        for j in range(i+1, l):
            if(a[j]<a[m]):
                m=j
        if(m!=i):
            a[i], a[m] = a[m], a[i]
    return a  

def bucketsort(a):
    bucket = []
    for _ in range(10):
        bucket.append([])
    l = len(a)
    for i in range(l):
        b_i = int(a[i]*10) 
        bucket[b_i].append(a[i])
    a=[] 
    for j in bucket:
        j = selsort(j) 
        a+=j
    return a


n = int(input("Enter no of students in first year: "))
lst = []
for i in range(n):
    print("Student", i+1, end = "")
    pt = float(input(", Enter percentage obtained(Eg. 98% = 0.98): "))
    lst.append(pt)
    


result = bucketsort(lst)
print(result)

print("\nTop 5 Scores are, ")
c=0
for _ in result[::-1]:
    if(c==5):
        break
    else:
        c+=1
        print(_, end = " ")