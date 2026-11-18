def num_letters(num_rows,num_columns):
    n_row=num_rows-2
    n_columns=num_columns-2
    center=n_row*n_columns
    return (num_rows*num_columns)-center
print(num_letters(3,4))
assert num_letters(3, 4) == 10  
print("Checking assertions.")
