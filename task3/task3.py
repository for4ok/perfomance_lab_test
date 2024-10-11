import json
import sys


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def fill_values(tests, values):
    # Создаем словарь для быстрого доступа по id
    values_dict = {value['id']: value['value'] for value in values}

    if isinstance(tests, dict):
        # Заполняем поле value для текущего теста, если он есть в values_dict
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]

        # Рекурсивно обрабатываем вложенные тесты
        if 'values' in tests:
            for subtest in tests['values']:
                fill_values(subtest, values_dict)

    elif isinstance(tests, list):
        for test in tests:
            fill_values(test, values_dict)


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values = load_json(values_file)['values']
    tests = load_json(tests_file)

    fill_values(tests, values)

    save_json(tests, report_file)


if __name__ == "__main__":
    main()
