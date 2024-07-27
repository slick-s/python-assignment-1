def hello():
    print('Hello')

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(list):
    if len(list) == 0:
        print('Zero')
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"Eating {list[0]}")
            else:
                print(f"Eating {list[i]}")


hello()
pack(3,3,3)
eat_lunch(['food', 'food2', 'food3'])