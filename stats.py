def get_num_words(text:str) -> int :
    words = text.split()
    return len(words)

def get_chars_dict(text:str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    return chars

# def get_sorted_dic(char_dict:dict[str, int]) -> list[dict[str, int]]:
#     list_dict = []
#     for char in char_dict:
#         dic = {}
#         if char.isalpha() :
#             dic[char] = char_dict[char]
#             list_dict.append(dic)
            
#     list_dict.sort(key = lambda d:list(d.values())[0], reverse=True)
#     return list_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
