# MARK: - Public methods

def is__not_numbers(list):
            for value in list:
                if not isinstance(value, (int, float)):
                    return True
            return False



# MARK: - Задание №1

def sum_distance(start: float, end: float, step: float = 1):
        """
        Sums all numbers from the 'start' value up to and including the 'end' value.

        If any of the input values are of type float, the result will be rounded
        to the 10th decimal place. 
        """
        if is__not_numbers([start, end, step]):
            return None
        
        if step <= 0:
             return None

        if start > end :
             start, end = end, start

        current_value = start
        result = 0
        while current_value <= end:
            result = round(result + current_value, 10)
            current_value = round(current_value + step, 10)
        
        return result

sum1 = sum_distance(1, 5) # == 15
sum2 = sum_distance(5, 1) # == 15
sum3 = sum_distance(1.1, 3) # == 3.2
sum4 = sum_distance(1.1, 3.3) # == 6.3
sum5 = sum_distance(1, 2, 0.1) # == 16.5



# MARK: - Задание №2

def trim_and_repeat(text: str, offset: int = 0, repetitions: int = 1):
     """
     Trims the string text starting from the position offset and repeats the result repetitions times.
    
    Use a type str for the text parameter to ensure predictable results.
    For the offset and repetitions parameters, use numeric values(int, float). If non-numeric values are provided,
    an empty string will be returned(return ""). float values will be converted to int.
     """
     if is__not_numbers([offset, repetitions]):
          return ""
     
     text = str(text)
     offset = int(offset)
     repetitions = int(repetitions)

     if not (0 <= offset < len(text)):
          return ""
     
     text_whith_offset = text[offset:]
     return text_whith_offset * repetitions