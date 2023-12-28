from decimal import Decimal
from enum import Enum
from datetime import datetime, timedelta
from collections import OrderedDict

# MARK: Constants (просто для удобства)
date_format = "%d.%m.%Y"
time_format = "%H:%M"


# MARK: - Transaction

class TypeTransaction(Enum):
    DEPOSITING = 1
    WITHDRAW = 2

class Transaction:
    #  Public properties
    @property
    def value(self):
        return self.__value
    
    @property
    def type_transaction(self):
        return self.__type_transaction
    
    @property
    def date_str(self):
        return self.__date.strftime(date_format)
    
    @property
    def full_date(self):
        return self.__date
    
    @property
    def is_success(self):
        return self.__is_success

    def __init__(self, type_transaction: TypeTransaction, value: Decimal, is_success: bool = True):
        self.__type_transaction = type_transaction
        self.__value = value
        self.__date = datetime.now()
        self.__is_success = is_success

    def __str__(self):
        return f"Transaction: type: {self.type_transaction.name}, value: {self.value}, is_success: {self.is_success}, date: {self.full_date}"


# MARK: - Histoty
# Пояснение:
# Можно было бы создать кастомную струкруту по типу стека (организация по принципу LIFO, последний пришел, первый вышел)
# Но мне захотелось использовать тут словарь (благо в Python это упорядоченная коллекция (c 3,7 версии))    
        
class HistotyTransaction:

    # MARK: Public properties
    @property
    def all_history_dict(self):
        return self.__history
    
    @property
    def last_transaction(self):
        last_key, last_value = OrderedDict(self.__history).popitem(last=True)
        if len(last_value) > 0:
            return last_value[-1]
        else:
            return None

    # MARK: Init
    def __init__(self, history: dict = {}):
        self.__history = history

    # MARK: Public methods
    def add_transaction(self, transaction: Transaction):
        date_transaction = transaction.date_str
        if date_transaction in self.__history:
            self.__history[date_transaction].append(transaction)
        else:
            self.__history[date_transaction] = [transaction]

    def get_histoty_for_date(self, date_str: str) -> [Transaction]:
        """
        Date format: '%d.%m.%Yж' ('01.01.2001'). Method can return None
        """
        return self.__history.get(date_str)
    
    def get_history_for_range(self, start_date_str: str, end_date_srt: str) -> dict:
        """
        Date format: '%d.%m.%Yж' ('01.01.2001'). Method can return None
        """

        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_srt, date_format)

        if start_date > end_date:
            return None
        
        result_dict = {}
        current_date = start_date

        while current_date <= end_date:
            key = current_date.strftime(date_format)
            if key in self.__history:
                result_dict[key] = self.__history[key]
            
            current_date += timedelta(days=1)
        
        return result_dict



# MARK: - Задание №1
    
class Account:

    # MARK: Publuc properties
    @property
    def current_balanse(self):
        return self.__current_balanse
    
    @property
    def last_transaction(self):
        return self.__history_transaction.last_transaction

    # MARK: Init
    def __init__(self, name: str, initial_balance: Decimal = 0, history_transaction: HistotyTransaction = HistotyTransaction()):
        self.__name = name
        self.__current_balanse = initial_balance
        self.__history_transaction = history_transaction

    # MARK: Public methods
    def depositing(self, value: Decimal):
        self.__current_balanse += value
        self.__history_transaction.add_transaction(Transaction(TypeTransaction.DEPOSITING, value))

    def withdraw(self, value: Decimal):
        if self.__current_balanse >= value:
            self.__current_balanse -= value
            self.__history_transaction.add_transaction(Transaction(TypeTransaction.WITHDRAW, value))
        else:
            self.__history_transaction.add_transaction(Transaction(TypeTransaction.WITHDRAW, value, is_success=False))
            raise ValueError("Недостаточно средств")
        
    def get_history_today(self):
        return self.__history_transaction.get_histoty_for_date(datetime.now().strftime(date_format))
    
    def get_history_for_date(self, date_str: str):
        "Формат даты: '01.01.2001' ('%d.%m.%Yж'), метод может вернуть None"
        return self.__history_transaction.get_histoty_for_date(date_str)
    
    def get_history_for_ragne(self, start_date_str: str, end_date_srt: str):
        "Формат даты: '01.01.2001' ('%d.%m.%Yж'), метод может вернуть None"
        return self.__history_transaction.get_history_for_range(start_date_str, end_date_srt)
