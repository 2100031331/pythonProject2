n=6
n1=0
n2=1
i=2
List=[n1,n2]
while i<n:
    nth=n1+n2
    List.append(nth)
    n1=n2
    n2=nth
    i=i+1
print(List)