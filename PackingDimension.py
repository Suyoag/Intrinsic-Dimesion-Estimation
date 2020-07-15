
# for i ← 1 to n do
# for j←1to|C|do
# if d(Sn[i],C[j])􏰂<rk then
# j←n+1
# if j<n+1then
# C ← C ∪{Sn[i]}
# Lk(l)=log|C|
# Dpack=-µ (L2)- µ (L1)/logr2-logr1
# If l > 10 and 1.65 (sqrt(sigma^2*L1)+sigma^2(l2))/sqrt(l(logr2-logr1))< dpack*(1-e)/2 then
#	Return Dpack
import statistics
import math
from statistics import variance
def calculator_dimension(r1, r2, Sn, e):
    SnLength = len(Sn)
    for l in range (1,9999999):
        perm = permutations(Sn)
        for k in range(1, 2):
            c = set()
            for i in range (1, len(Sn)):
                for j in range (1, abs(c)):
                    if "d(sn[i], C[j]) < rk"
                        j= snlength + 1
                    if j<n+1
                        C= c.union(sn(i))
                L(l)=math.log(abs(c))
            Dpack= statistics.mean(L(l))- statistics.mean(L(l))/math.log(r2)-math.log(r1)
        if l > 10 and 1.65*math.sqrt(variance(L1)+variance(L2))/math.sqrt(l)*(math.log(r2)-math.log(r1))<Dpack*(1-e)/2                   
    return (Dpack)


calculator_dimension()
