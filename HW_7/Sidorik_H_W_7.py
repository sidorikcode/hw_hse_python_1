import re

#  MARK: - Helper
def log_result_check_validate_car_id(result: tuple):
    if result:
        (resultt, resulttt) = result
        print(f"Номер {resultt} валиден. Регион: {resulttt}")
    else:
        print(f"Номер не валиден")


# MARK: - Задание №1

def validate_car_id(car_id):
    pattern = r"^[АВЕКМНОРСТУХABEKMHOPCTYX]{1}\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2,3}$"
    
    if re.match(pattern, car_id, re.IGNORECASE):
        number = car_id[:6].upper()
        region = car_id[6:]
        return (number, region)
    else:
        return None


car_id_1 = "А222BС96"
result_1 = validate_car_id(car_id_1)
log_result_check_validate_car_id(result_1)


car_id_2 = "АБ22ВВ193"
result_2 = validate_car_id(car_id_2)
log_result_check_validate_car_id(result_2)

car_id_3 = "a224bb13"
result_3 = validate_car_id(car_id_3)
log_result_check_validate_car_id(result_3)

