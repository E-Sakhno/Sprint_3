import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError("Позиция отсутствует в чеке")
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        sum_total = sum(total)
        if len(total) > 10:  # можно сравнить не total, а self.__number_items
            return sum_total * 0.9
        else:
            return sum_total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        sum_nds = sum(twenty_percent_tax) * 0.2
        if self.__number_items > 10:
            # можно сначала просуммировать товары, учесть скидку и рассчитать НДС
            # но items * 0.9 * 0.2 == items * 0.2 * 0.9
            # поэтому просто умножаю НДС на 0.9
            return sum_nds * 0.9
        else:
            return sum_nds
        
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        sum_nds = sum(ten_percent_tax) * 0.1
        if self.__number_items > 10:
            return sum_nds * 0.9
        else:
            return sum_nds
