from pprint import pprint
import os


def prepare_dict(file_name):
    with open(file_name, encoding='utf-8') as f:
        result_dict = {}
        for line in f:
            dish = line.rstrip()
            result_dict[dish] = []
            for i in range(int(f.readline())):
                ingredient, quantity, units = f.readline().rstrip().split(' | ')
                result_dict[dish].append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': units})
            f.readline()
        return result_dict


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    result_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            units = ingredient['measure']
            quantity = float(ingredient['quantity']) if '.' in ingredient['quantity'] else int(ingredient['quantity'])
            quantity *= person_count
            if name in result_dict:
                result_dict[name]['quantity'] += quantity
            else:
                result_dict[name] = {'measure': units, 'quantity': quantity}
    return result_dict


def join_files(folder_name):
    files_info = []

    for filename in os.listdir(folder_name):
        with open(os.path.join(folder_name, filename), encoding="utf-8") as f:
            num_lines = sum(1 for line in f)
            files_info.append((num_lines, filename))
    files_info.sort()

    with open('result_file.txt', 'w', encoding='utf-8') as f:
        for file in files_info:
            lines, name = file
            f.write(f"{name}\n{lines}\n")
            with open(os.path.join(folder_name, name), encoding='utf-8') as content:
                for line in content:
                    f.write(line)
                if not line.endswith('\n'):
                    f.write('\n')


def main():
    cook_book = prepare_dict('recipes.txt')
    pprint(get_shop_list_by_dishes(['Запеченный картофель', "Омлет"], 2, cook_book))
    join_files('files')


if __name__ == "__main__":
    main()
