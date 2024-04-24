# lab 5 var. 6
# function 1
def offset_generator(input_list, offset_value):
    for item in input_list:
        yield item + offset_value


# function 2
def lazy_replacement_generator(input_list, replacement_func):
    for item in input_list:
        yield replacement_func(item)


# function 3 (combination)
def combined_generator(input_list, offset_value, replacement_func):
    result_of_func = offset_generator(input_list, offset_value)
    for result_of_func in lazy_replacement_generator(result_of_func, replacement_func):
        yield result_of_func


# example of using :
def square(x):
    return x * x


# input_list:
my_list = [1, 2, 3, 4, 5]

# combined genarator :
combined = combined_generator(my_list, 4, square)

# print the result if necessary
for result in combined:
    print(result)
