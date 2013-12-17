def main(A,B):
    sumA=0
    for i in A: sumA=sumA+i
    sumB=0
    for i in B: sumB=sumB+i
    
    if len(A)==len(B) and sumA==sumB:
        n=len(A)
        print(A,end=' ')
        
        while not A==B:
            C=[]
            for i in range(n):
                C.append(0)
                C[i]=A[i]-B[i]
                            
            i=0
            while not C[i]<0:
                i=i+1
            k=i
            while not C[k]>0:
                k=k-1
            A[k]=A[k]-1
            A[i]=A[i]+1
            print(A,end=' ')
    else:
        print("Invalid A and B.")
