from functools import reduce

lst_of_characters = [(1, 'a'), (1, 'b'), (0, 'c'), (1, 'd'), (1, 'a'), (0, 'b')]


def reduction_function(result_from_previous_iteration,
                       new_variable_to_add):
    print('result_so_far', result_from_previous_iteration)
    print('new_variable', new_variable_to_add)
    category = new_variable_to_add[0]
    if category not in result_from_previous_iteration:
        result_from_previous_iteration[category] = {}

    if new_variable_to_add[1] not in result_from_previous_iteration[category]:
         result_from_previous_iteration[category][new_variable_to_add[1]] = 1
    else:
        result_from_previous_iteration[category][new_variable_to_add[1]] += 1
    print('res', result_from_previous_iteration)
    print('------')
    return result_from_previous_iteration


print('final', reduce(reduction_function, lst_of_characters, {}))

