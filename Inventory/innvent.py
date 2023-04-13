import csv

if __name__ == '__main__':
    # Считываем данные из файла
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Создаем словарь, где ключами являются категории
        categories = {}
        # Создаем словарь, где ключами являются бренды
        brands = {}
        for row in reader:
            # Добавляем товар в словарь категорий
            if row['category'] not in categories:
                categories[row['category']] = []
            categories[row['category']].append(row)
            # Добавляем товар в словарь брендов
            if row['brand'] not in brands:
                brands[row['brand']] = []
            brands[row['brand']].append(row)

        # Выводим статистику по брендам
        print('Статистика по брендам:')
        for brand in brands:
            print(f"- Від бренду \"{brand}\" є {len(brands[brand])} товарів")

        # Выводим статистику по категориям
        print('Статистика по категоріям:')
        for category in categories:
            print(f"- Серед категорії \"{category}\" є {len(categories[category])} товарів")

        # Выводим информацию о товарах заданного бренда
        selected_brand = 'Samsung'
        print(f'Інформація про товари бренду "{selected_brand}":')
        for row in brands[selected_brand]:
            print(row)

        # Выводим информацию о товарах заданной категории
        selected_category = 'Smartphones'
        print(f'Інформація про товари категорії "{selected_category}":')
        for row in categories[selected_category]:
            print(row)

        # Распределяем товары по брендам для каждой категории
        print('Розподіл товарів по брендам для кожної категорії:')
        for category in categories:
            # Создаем словарь, где ключами являются бренды
            brands_in_category = {}
            for row in categories[category]:
                # Добавляем товар в словарь брендов
                if row['brand'] not in brands_in_category:
                    brands_in_category[row['brand']] = 1
                else:
                    brands_in_category[row['brand']] += 1
            print(f"- У категорії \"{category}\" представлені товари таких брендів: ", brands_in_category)
