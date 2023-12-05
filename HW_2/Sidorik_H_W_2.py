from typing import Dict, List, Set

# MARK: - Задание №1

def log_unique_geotags(users_and_geotag_dict: Dict[str, List[int]]):
    set_geotag: Set[int] = set()
    for geotag in users_and_geotag_dict.values():
        set_geotag.update(geotag)
    
    if not set_geotag:
        print("Error! Dict is empty")
    else:
        print(set_geotag)


ids = {
    "user1": [213, 213, 213, 15, 213], 
    "user2": [54, 54, 119, 119, 119], 
    "user3": [213, 98, 98, 35]
}

ids_empty = {}

log_unique_geotags(ids)
log_unique_geotags(ids_empty)



# MARK: - Задание №2

def log_count_test(queries: List[str]):
    if not queries:
        print("Error! List is empty")
    dict: Dict[int, int] = {}

    for query in queries:
        count_word = len(query.split())
        dict[count_word] = dict.get(count_word, 0) + 1

    result = ""
    for key in sorted(dict.keys()):
        precentage = dict[key] / len(queries) * 100
        result += f"Поисковых запросов, содержащих {key} слов(а): {precentage: .2f}%\n"

    print(result)


queries = [
    "смотреть сериалы онлайн",
    "новости спорта",
    "афиша кино",
    "курс доллара",
    "сериалы этим летом",
    "курс по питону",
    "сериалы про спорт",
]

queries_empty = []

log_count_test(queries)
log_count_test(queries_empty)