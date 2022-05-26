# BÀI 5
# 5.1
##file:  mymath.py##
def square(n):
    return n*n
def cube(n):
    return n*n*n
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
        return float(sum)/nvals
# 5.2
import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('day '+str(t1.day))
print('month '+str(t1.month))
print('minute'+str(t1.minute))
print('second'+str(t1.second))

#define todays date and time
t2 = dt.datetime.now()
diff = t2-t1
print('how many days difference? ' + str(diff.days))

# 5.3
import numpy as np
x = np.arange(12, 38)
reversed_string=x[::-1]

print(reversed_string)

# 5.7
import numpy as np
data_type=[('name', 'S15'),('lass',int),('height',float)]
students_details=[('james',5,48.5), ('nail',6,52.5),('paul',5,42.10), ('pit',5,40.11)]
#create a structured array
students=np.array(students_details,dtype=data_type)
print("original array:")
print(students)
print("sort by height")
print(np.sort(students, order='height'))
