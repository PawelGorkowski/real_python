def print_vector(x, y, z):
    print(f'{x}, {y}, {z}')


# if __name__ == "__main__":
#     print_vector(1, 0, 1)


tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
gen_expr = (x * x for x in range(3))

# # equvalent to -> print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
# print_vector(*tuple_vec)
# print_vector(*list_vec)
# print_vector(*gen_expr)

# # doesn't work if arg not called x,y,z like in function
# dict_vec = {'x': 1, 'y': 2, 'z': 3}
# print_vector(**dict_vec)
# print_vector(*dict_vec)
