def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    operations = list(map(lambda x: x.split()[1], problems))
    if any(op not in ['+', '-'] for op in operations):
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []
    for i in problems:
        parts = i.split()
        numbers.extend([parts[0], parts[2]])

    if not all(map(str.isdigit, numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(len(num) <= 4 for num in numbers):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    bottom_row = ''
    dashes = ''
    solutions = ''
    for index, i in enumerate(problems):
        parts = i.split()
        num1, operator, num2 = parts
        space_width = max(len(num1), len(num2)) + 2

        top_row += num1.rjust(space_width)
        bottom_row += operator + num2.rjust(space_width - 1)
        dashes += '-' * space_width
        if val:
            solution = str(eval(i))
            solutions += solution.rjust(space_width)

        if index != len(problems) - 1:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4
            if val:
                solutions += ' ' * 4

    if val:
        arranged_problems = '\n'.join([top_row, bottom_row, dashes, solutions])
    else:
        arranged_problems = '\n'.join([top_row, bottom_row, dashes])
    return arranged_problems
