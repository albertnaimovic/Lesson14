# 1. Create a simple program that would log all inputs from the terminal. Configs must show all additional data (time, date, level etc.)

# import logging
# logging.basicConfig(level=logging.DEBUG,filename='1_task.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# while True:
#     my_input = input("Enter something: ")
#     logging.info(my_input)


# from typing import List

# import logging
# logging.basicConfig(level=logging.DEBUG,filename='2_task.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# def move_to_end(my_list: List[int], my_type: int) -> List[int]:
#     without_my_type: list = [x for x in my_list if x != my_type]
#     extract_my_type: list = [x for x in my_list if x == my_type]
#     without_my_type.extend(extract_my_type)
#     logging.info(f"Input: {my_list, my_type} -> Result: {without_my_type}")
#     return without_my_type

# print(move_to_end([1, 3, 2, 4, 4, 1], 1))

# 5. Setup accounting software , that would take annual income , expenses , VAT rate (all values must be floats) and calculate profit,
# paid taxes in 4 different currencies (USD, EU, JPY, CNY). All calculations and results should be printed on screen. All data and possible errors must be logged to a file.


import logging
from typing import List
import requests
API_KEY = "7b305a85fb112f3b93e6d738c24d5803"


logging.basicConfig(level=logging.DEBUG, filename='vmi.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
def get_expenses() -> List[float]:
    paid = []    
    while True:
        expen = input("Please enter your expenses: ")
        if expen.isnumeric():
            paid.append(float(expen))
            logging.debug(f"Expences entered: {expen}")
        else:
            logging.debug(f"Expences in total entered: {paid}")
            logging.debug(f"Sum of expences: {sum(paid)}")
            print(f"Sum of expences: {sum(paid)}")
            return sum(paid)


def get_anual_income()-> float:
    anual_income = input("Please enter your anual income: ")
    if anual_income.isnumeric():
        return float(anual_income)
    else:
        raise ValueError("Bad value antered")


def calculate_profit(income: float, expenses: float, vat: int) -> float:
    ebita = income - expenses
    profit = ebita * (100 - vat) / 100
    logging.info(f"The profit is: {profit}")
    return profit


def exchange_curency(value: float, curency: str) -> float:
    curency_rate = get_curency_exchange_rate(curency)
    logging.info(f"Exchange rate for {curency}: {curency_rate}")
    return value * curency_rate


def get_curency_exchange_rate(name: str) -> float:
    result = requests.get(f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={name}") 
    logging.info(f"Respond from API: {result.json()}")
    if not result.json()["success"]:
        raise ValueError("Please specify curency code")
    return result.json()["rates"][name]


expences = get_expenses()
anual_income = get_anual_income()
requested_curency = input("Please enter curency name USD, EU, JPY, CNY: ")
profit = calculate_profit(anual_income, expences, 15)


try:
    cur = exchange_curency(profit, requested_curency)
    print(cur)
except ValueError:
    print("Bad exchange code name")