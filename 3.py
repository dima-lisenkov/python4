input_list = [int(x) for x in input('Введите последовательность: ').split()]
def ExplitDoubles(input_list):
    explit_list = []
    result_list = []
    for _ in range(len(input_list)):
        elem = input_list.pop(0)
        if (elem in input_list) or (elem in explit_list):
            explit_list.append(elem)
        else:
            result_list.append(elem)

    return result_list


print(f'Для последовательности {input_list}: {ExplitDoubles(input_list)}')