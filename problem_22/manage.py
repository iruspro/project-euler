import value
import sorting


path = 'p022_names.txt'
list_names = sorting.get_list_names(path)
amount = value.get_amount_name_scores(list_names)
print(amount)
