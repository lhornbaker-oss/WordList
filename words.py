def num_letters(num_rows,num_columns):
    row=num_rows-2
    column=num_columns-2
    center=row*column
    return (num_rows*num_columns)-center
print(num_letters(3,4))
assert num_letters(3, 4) == 10  
print("Checking assertions.")

import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words=[]
rows,columns=data.shape
for c in range(columns):
    words.append(str(data[0,c]))
for r in range(1,rows-1):
    words.append(str(data[r,columns-1]))
for c in range(columns):
    words.append(str(data[rows-1,c]))
for r in range(1,rows-1):
    words.append(str(data[r,0]))
    
print ("w",words)
print(num_letters(rows, columns))
assert len(words) == num_letters(rows, columns) 
