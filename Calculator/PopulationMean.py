def mean(pop):
    sum = 0
    p = 0
    for row in pop:
        p = p + 1
        sum = sum + row # row updating by the next value. pop being list of 5 elements, row being 1 initially for 1st iteration and so on
    return sum / p