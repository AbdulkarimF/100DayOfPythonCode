# Problems
print("Problem 1")
def function(P, N):
    if (P>0):
        result= N*function(P-1, N)
    else:
        result=1
    return result
print("5^3 equal:")
print(function(3, 5))
print("\nProblem 2")
List = [-4,-6, -5, -1, 2, 3, 7, 9, 88]
PositiveList = []
for n in List:
    f = lambda x: PositiveList.append(x) if x>0 else None
    f(n)
print(PositiveList)
