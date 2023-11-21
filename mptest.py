import multiprocessing as mp
import time
import math
import concurrent.futures
import itertools
results_a = []
results_b = []
results_c = []

def make_calculation_one(number):
    return math.sqrt(math.sqrt(number ** 20))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    
    y = 1000000
    print('Number',format(y,','))
    number_list = list(range(y))

    # First method
    start = time.time()
    for i in number_list: results_a.append(make_calculation_one(i))
    # make_calculation_two(number_list)
    # make_calculation_three(number_list)
    end = time.time()
    finalTime1 = end - start
    print(finalTime1)

    seta1 =  []
    setb1 = []
    setc1 = []
    # print(seta1)
    # Second method
    start = time.time()
    newlst1 = number_list[:len(number_list)//2]
    newlst2 = number_list[len(number_list)//2:]
    # print(newlst1, newlst2)
    q = mp.Queue()
    def fun(lst,qe):
        for i in lst:
            qe.put(make_calculation_one(i))
    p1 = mp.Process(target=fun, args=(newlst1,q,))
    p2 = mp.Process(target=fun, args=(newlst2,q,))
    # p2 = mp.Process(target=make_calculation_one, args=(number_list,q))
    # p3 = mp.Process(target=make_calculation_three, args=(number_list,))
    p1.start()
    p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    for i in q:
        seta1.append(q.get())
    end = time.time()
    finalTime2 = end - start
    print(finalTime2)

    seta2 =  results_a
    setb2 = results_b
    setc2 = results_c
    

    # Third method
    
    def splitToSize(lst):
        current = []
        while len(lst) > 0:
            x = None
            workObj = lst.pop()
            if len(current) < 999:
                current.append(workObj)
            else:
                current.append(workObj)
                x = current
                current = []
                yield x
        return x
    
    

    start = time.time()
    # listoflist = splitToSize(number_list)
    # print(number_list)
    # print(len(listoflist))
    with concurrent.futures.ProcessPoolExecutor() as executor:

        # def send(lista):
        #     f1 = executor.submit(make_calculation_one, lista)
        #     f2 = executor.submit(make_calculation_two, lista)
        #     f3 = executor.submit(make_calculation_three, lista)
        # for _ in splitToSize(number_list):
        #     # print(_,len(_))
        #     send(_)
        f1 = executor.submit(make_calculation_one, number_list)
        # f2 = executor.submit(make_calculation_two, number_list)
        # f3 = executor.submit(make_calculation_three, number_list)
        
    end = time.time()
    seta3 =  results_a
    setb3 = results_b
    setc3 = results_c
    finalTime3 = end - start
    print(finalTime3)
    print(seta1==seta2==seta3)
    print(setb1==setb2==setb3)
    print(setc1==setc2==setc3)
    print(setc1,setc2,setc3)
    print(f"Improvement mehotd 2 {round(finalTime2/finalTime1*100, 2)-100}%")
    print(f"Improvement mehotd 3 {round(finalTime3/finalTime1*100, 2)-100}%")