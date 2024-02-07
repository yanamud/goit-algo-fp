items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

################## жадібний алгоритм ####################################
class Item:
    def __init__(self, items):
        self.cost = items['cost']
        self.calories = items['calories']
        self.name = items['name']

def greedy_algorithm(items, capacity) :
    lst = []
    for elems in items.items():
        name ,cost, calories = elems[0], elems[1]['cost'], elems[1]['calories']
        lst.append(Item({"name": name, "cost": cost, "calories": calories}))
        sorted(lst, key=lambda x: x.calories/x.cost, reverse=True)
        
    total_menu = []
    total_budget = 0
    total_value = 0
    for item in lst:
        if capacity >= item.cost:
            capacity -= item.cost
            total_menu.append(item.name)
            total_budget += item.cost
            total_value += item.calories
            
    return total_menu, total_budget, total_value, capacity

# Бюджет
capacity = 105
# Виклик функції
res = greedy_algorithm(items, capacity)
print('-------------------------------------------------------------------')
print('Результати запуску жадібного алгоритму:')
print('-------------------------------------------------------------------')
print(f'\nЗгідно наданого бюджету в розмірі {capacity}')
print('з урахуванням максимізації співвідношення калорій до вартості можна придбати:')
print(res[0])
print(f'\nЗагальна вартість придбаного кошику:')
print(res[1])
print(f'\nЗагальна калорійність придбаного кошику:')
print(res[2])
print(f'\nЗалишок бюджету:')
print(res[3])
print('-------------------------------------------------------------------')

################## алгоритм динамічного програмування ######################

def dynamic_programming(items, capacity):
    price = []
    value = []
    lst = []

    for elems in items.items():
        name ,cost, calories = elems[0], elems[1]['cost'], elems[1]['calories'] 
        lst.append(name)   
        price.append(cost)
        value.append(calories)

    n = len(value) # знаходимо розміри таблиці

    # створюємо табрицю із нульових значень
    V = [[0 for a in range(capacity+1)] for i in range(n+1)]    

    for i in range(n+1):
        for a in range(capacity+1):
            if i == 0 or a == 0:
                V[i][a] = 0

            # якщо ціна предмета меньще бюджета,
            # максимізуємо значення сумарної калорійності
            elif price[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a-price[i-1]], V[i-1][a])

            # якщо ціна предмета більша бюджета,
            # забираємо значення комірки із попереднього елемента
            else:
                V[i][a] = V[i-1][a]  

    res = V[n][capacity]  # останій елемент таблиці

    a = capacity          # максимальний бюджет
    items_list = []       # список ціни, калорійності, назви предметів
    
    for i in range(n, 0, -1):  # рухаємось в зворотньому напрямку
        if res <= 0:  
            break
        if res == V[i-1][a]:  
            continue
        else:
            # "забираємо" предмет з його атрибутами
            items_list.append((price[i-1], value[i-1], lst[i-1]))

            res -= value[i-1]   # зменщуємо калорийність
            a -= price[i-1]  # щменшуємо бюджет
           
    selected_stuff = []
    total_budget = 0
    # знаходимо назву та фактичний бюджет предметів
    for search in items_list:
        selected_stuff.append(search[2])
        total_budget += search[0]
            
    return selected_stuff, total_budget, V[n][capacity], a

# Бюджет
capacity = 105
# Виклик функції
res = dynamic_programming(items, capacity)

print('Результати запуску динамічного програмування:')
print('-------------------------------------------------------------------')
print(f'\nЗгідно наданого бюджету в розмірі {capacity}')
print('з урахуванням максимізації калорійності можна придбати:')
print(res[0])
print(f'\nЗагальна вартість придбаного кошику:')
print(res[1])
print(f'\nЗагальна калорійність придбаного кошику:')
print(res[2])
print(f'\nЗалишок бюджету:')
print(res[3])
print('-------------------------------------------------------------------')