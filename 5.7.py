import numpy as np
data_type=[('name','s15'),('class',int),('height',float)]
students_details=[('james',5,48.5),('gsah',4,45.1),('yqu',3,53.67)]
students=np.array(students_details,dtype=data_type)
print("original array")
print(students)
print('sort by height')
print(np.sort(students,order='height'))