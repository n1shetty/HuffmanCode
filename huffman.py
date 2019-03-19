"""
Created on Sat Mar 16 20:44:21 2019
@author: Nishanth Shetty
"""
p = [0.4, 0.2, 0.2, 0.1, 0.1]
p_ = p
p.sort(reverse = True)
end_ = len(p) - 1
d_ = []
q = []
l = []
L = []
P = []
Q = []
Q_ = []

for i in range(1, end_+2):
    l.append(str(i))
print(p, l)
L.append(l)
P.append(p)

while(end_>=2):
    
    compare = end_-2
    p[end_-1] = p[end_]+p[end_-1]
    p[end_] = 0

    while(compare >= 0):
        if(p[end_-1]>= p[compare]):
            indx = compare
        compare = compare - 1 
    
    tmp_1 = p[0:indx]
    tmp_2 = [p[end_ - 1]]
    tmp_3 = p[indx:end_ - 1]
    p = tmp_1+tmp_2+tmp_3
    P.append(p)
    
    tmp_1 = l[0:indx]
    tmp_2 = [[l[end_ - 1], l[end_ ]]]
    tmp_3 = l[indx:end_ - 1]
    l = tmp_1+tmp_2+tmp_3
    d_ = ["".join(x) if type(x) == list else x for x in l  ]
    l = d_
    L.append(l)
    
    print("p = {}, l = {} ".format(p, l))
    end_ = end_ - 1

for i in range(1, len(p_)+1):
    Q = []
    r = len(L) - 1  
    while(r >= 0):

        for u in range(len(L[r])):            

            if ((str(i) in L[r][u]) == True):
               
                if(u == len(L[r])-1):
                    #print(Q[i])
                    Q.append('1')  
                elif(u == len(L[r])-2):
                    Q.append('0')  
                else:
                    Q.append('')
        r = r - 1
    Q_.append(''.join(Q))
print(Q_)