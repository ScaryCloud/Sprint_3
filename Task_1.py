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
        try: 
            self.__name_items.append(name)
            if len(name) == 0 or len(name) > 40: 
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__number_items += 1
        except (ValueError, NameError) as e:
            print(e)

    def delete_item_from_check(self, name):
        try: 
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name) 
                self.__number_items -= 1
        except NameError as a:
            print(a)

    def check_amount(self):
        total = []
        total_sum = 0
        for item in self.__name_items:
            key = item.lower() 
            if key in self.__item_price:
                total.append(self.__item_price[key])

        for price in total:
            total_sum += price

        if len(total) > 10:
            total_sum = total_sum * 0.9
        print(total_sum)
        return total_sum

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        sum_nds = 0
        for item in self.__name_items:
            key = item.lower() 
            if key in self.__tax_rate and self.__tax_rate[key] == 10:
                ten_percent_tax.append(key) 
                total.append(self.__item_price[key]) 
        for price in total:
            if len(self.__name_items) > 10: 
                price = price * 0.9 
            sum_nds += price * 0.1
        return sum_nds

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        sum_nds = 0
        for item in self.__name_items:
            key = item.lower() 
            if key in self.__tax_rate and self.__tax_rate[key] == 20:
                twenty_percent_tax.append(key) 
                total.append(self.__item_price[key]) 
        for price in total:
            if len(self.__name_items) > 10:
                price = price * 0.9
            sum_nds += price * 0.2

        return sum_nds 

    def total_tax(self):
        total_sum_nds = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        print(total_sum_nds)
        return total_sum_nds

    def get_telephone_number(self, telephone_number):
        str_tlf = str(telephone_number)
        try:
            tel_str = str(telephone_number)   
            if not tel_str.isdigit():         #тут мне подсказала нейронка но я пытался
                raise ValueError('Необходимо ввести цифры') 
            if len(tel_str) != 10: 
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            print(f"+7{tel_str}") 
            return f"+7{tel_str}"
        except ValueError as e:
            print(e)


cheque = OnlineSalesRegisterCollector()
cheque.add_item_to_cheque('чипсы')
cheque.add_item_to_cheque('кола')
cheque.add_item_to_cheque('печенье')
cheque.add_item_to_cheque('чипсы')
cheque.add_item_to_cheque('чипсы')
cheque.add_item_to_cheque('чипсы')
cheque.add_item_to_cheque('чипсы')
cheque.add_item_to_cheque('молоко')
cheque.add_item_to_cheque('кефир')
cheque.add_item_to_cheque('кефир')
cheque.add_item_to_cheque('молоко')
cheque.add_item_to_cheque('чипсы')
cheque.check_amount()
cheque.twenty_percent_tax_calculation()
cheque.ten_percent_tax_calculation()
cheque.total_tax()
cheque.get_telephone_number('Розовый айфончик 18 pro max')