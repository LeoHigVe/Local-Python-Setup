def hello():
    print("Hello World")

def pack(a,b,c):
    return [a,b,c]
def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("my lunch box empty")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First i eat {my_lst[0]}")
            else:
                print(f"Next i eat {my_lst[i]}")

hello()
print(pack(1,2,3))
print(pack("a","b","c"))
eat_lunch([])
eat_lunch(["jorts"])
eat_lunch(["sandwich","apple","candy"])
