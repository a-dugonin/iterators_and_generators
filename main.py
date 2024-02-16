from task_1.number_squares import user_value, NumberSquares, number_squares, number_squares_gen_expression
if __name__ == '__main__':
    number_squares_iterator = NumberSquares(user_value)
    print(*number_squares_iterator)

    number_squares_func_generator = number_squares(user_value)
    print(*number_squares_func_generator)

    print(*number_squares_gen_expression)
