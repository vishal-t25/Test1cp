from collections import defaultdict
def main():
    inp = list(str(input()))

    num_dict = defaultdict(int)

    for i in inp:
        a = int(i)
        num_dict[a] += 1

    for n in range(1,10):
        if num_dict[n] == 0:
            print(n)
            return

    

    vals = list(num_dict.items())

    vals.sort(key = lambda x: (x[1],x[0]))
    
    if num_dict[0] == 0:
        print(vals[0][0],end="")
        num_dict[vals[0][0]] -=1
        print(0,end = "")
        while num_dict[vals[0][0]] > 0:
            print(vals[0][0],end="")
            num_dict[vals[0][0]] -= 1 
    elif vals[0][0] == 0:
        if vals[0][1] + 1 >= vals[1][1]:
            while num_dict[vals[1][0]] >= 0:
                print(vals[1][0],end="")
                num_dict[vals[1][0]] -= 1
        else:
            print(1, end= "")
            while num_dict[vals[0][0]] >= 0:
                print(0,end="")
                num_dict[vals[0][0]] -= 1
    else:
         while num_dict[vals[0][0]] >= 0:
            print(vals[0][0],end="")
            num_dict[vals[0][0]] -= 1

main()