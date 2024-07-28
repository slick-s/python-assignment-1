def max_num(a,b,c):
    return max([a,b,c])

def multi_list(list):
    if len(list) == 0:
        return 0
    
    product = list[0]

    if len(list) > 1:
        for i in list[1::]:
            product *= i

    return product

print(multi_list([1,2,3]))

def reverse_str(str):
    return str[::-1]


print(reverse_str('112'))

def num_within(a,b,c):
    return c in range(a,b+1)


print(num_within(5,7,9))

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)