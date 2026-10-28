from itertools import permuatations
num_ops, min_ret = map(int,input().split())

cost_prof = []



for _ in range(num_ops):
    cost, prof = map(int, input().split())

    cost_prof.append([cost,prof])
    

min_days = float('inf')

for p in permuatations(cost_prof):
    tc = 0 
    prof_per_day = 0
    for each in p:
        tc += each[0]
        prof_per_day += each[1]


    



    
