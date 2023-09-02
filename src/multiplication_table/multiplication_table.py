
def multiplication_table(num):
    row = [x for x in range(num+1)]
    mul_table = [row]

    for col in range(1,num+1):
        new_row = [x*row[col] for x in range(1,num+1)]
        new_row.insert(0,row[col])
        mul_table.append(new_row)
  
    return mul_table

def multiplication_table_mod_Z(num):
    row = [x for x in range(num)]
    mul_table = [row]

    for col in range(1,num):
        new_row = [x*row[col]%num for x in range(1,num)]
        new_row.insert(0,row[col])
        mul_table.append(new_row)
  
    return mul_table

