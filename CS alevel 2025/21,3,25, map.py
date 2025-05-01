def square(num):
    return num**2
def own_map(f, orig_list:list):
    return [f(orig_list[i]) for i in range(len(orig_list))]

print(own_map(square, [1,2,3]))