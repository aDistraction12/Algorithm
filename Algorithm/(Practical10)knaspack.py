print("Name : Sumit Singh\nRoll No : 4354\n")

def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 
# end of function knapSack
 
 
#Driver Code
val=[25,50,75,100,125,150,175,200]
wt=[20,30,40,50,60,70,80,90]
W = 50
n = len(val)
print("Maximum Value :")
print (knapSack(W, wt, val, n))
