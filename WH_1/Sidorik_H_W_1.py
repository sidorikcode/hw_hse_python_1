# MARK: - Задание #1

def log_midle_ch_in_word(word: str):
    if not word:
        print("Error, word is empty")
        return

    if len(word) == 1:
        print(word)
        return
    
    is_even = len(word) % 2 == 0

    midle_index = len(word) // 2
    middle_ch = word[midle_index]
    
    result = middle_ch if not is_even else word[midle_index - 1] + middle_ch
    print(result)

empty_word = ""
single_ch = "J"
two_ch = "Jo"
not_even_str = "Jon"
even_str = "Ilia"
log_midle_ch_in_word(empty_word)
log_midle_ch_in_word(single_ch)
log_midle_ch_in_word(two_ch)
log_midle_ch_in_word(not_even_str)
log_midle_ch_in_word(even_str)


# MARK: - Задание №2

def logBestRecommendations(boys: list[str], girls: list[str]):
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары!")
        return
    
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)

    display_text = "Идеальные пары:\n"
    for i, boy in enumerate(sorted_boys):
        girl = sorted_girls[i]
        
        display_text += boy + " и " + girl + "\n"
    
    print(display_text)


boys = ["Peter", "Alex", "John", "Arthur", "Richard"] 
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

boys_2 = ["Peter", "Alex", "John", "Arthur", "Richard", "Michael"] 
girls_2 = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

logBestRecommendations(boys, girls)
logBestRecommendations(boys_2, girls_2)

