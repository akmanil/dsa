prev1 =0;
prev2 = 1;

for fibo in range(18):
    newfibo = prev1+ prev2; 
    print(newfibo);
    prev1 =prev2;
    prev2 = newfibo;

# using recursion
count = 2;
print(0);
print(1);
def fibonaci(a,b):
    global count;
    if(count<20):
        newfibonaci = a+ b;
        print(newfibonaci);
        a = b;
        b=newfibonaci;
        count += 1;
        fibonaci(a,b); #this is the fibonnaci function
    else:
        return

fibonaci(0,1);
