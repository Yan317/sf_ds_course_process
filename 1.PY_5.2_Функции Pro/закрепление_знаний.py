# Раздел "Закрепление знаний"
# финальное Задание 4.8
def register(surname, name, date, middle_name = None, registry = []):
    def check_date(day, month, year):
        def is_leap(year):
            if year % 400 == 0: return True
            if year % 4 == 0:
                if year % 100 == 0:
                    return False
                else:
                    return True
            return False
    
        if type(day) is not int: return False
        if type(month) is not int: return False
        if type(year) is not int: return False
    
        if year < 1900 or year > 2022: return False

        if month < 1 or month > 12: return False

        if day < 1 or day > 31: return False

        if month in (4, 6, 9, 11) and day > 30: return False

        if month == 2:
            if is_leap(year):
                if day > 29: return False
            else:
                if day > 28: return False
        
        return True
    
    if not check_date(*date):
        raise ValueError('Invalid Date!')
    
    registry.append((surname, name, middle_name, *date))
    return registry

print(register(surname = 'Иванов', name = 'Сергей', date = (12, 8, 2000), middle_name = None, registry = None))