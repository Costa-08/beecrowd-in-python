n=int(input())
i=1
n1seq=int(input())
Seq=[n1seq]
while i!=n:
    nseq=int(input())
    k=len(Seq)
    if nseq!=Seq[k-1]:
        Seq.append(nseq)
    i=i+1
print(len(Seq))
