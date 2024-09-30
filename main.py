# put your python code here
# put your python code here
import random
with open('input.txt', 'r') as file1, open('output.txt', 'w') as wrr:
    m = [n.rstrip() for n in file1.readlines()]
    #print([n for n in file1.readlines()], file = wrr)

    #print(F"{1}) {m}", file=wrr)
    for i in range(1, len(m)):
        #wrr.write(i,') ', m[i-1])
        print(F"{i}) {m[i-1]}", file=wrr)

        #file.write(str(random.randint(111,778)))
        #print(file=file)
        #print('asddad', file=wrr)
