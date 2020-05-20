import re
import pprint

def get_word_count(text) -> list:
    str = re.sub(r'[\W]]', ' ', text).lower()
    word_list = str.split(' ')
    word_dict = {}
    for i in word_list:
        if i not in word_dict:
            word_dict[i] = 0
        word_dict[i] += 1
    return sorted(word_dict.items(), key=lambda d:d[1], reverse=True)

def get_text(file_url):
    with open(file_url, mode='r') as f:
        return f.read()

def save_text(file_url, content:list):
    with open(file_url, mode='w') as f:
        for k,v in content:
            f.write(f'key is {k} and value is {v} \n')

s1 = get_word_count(get_text('word_count_in.txt'))
save_text('word_count_out.txt', s1)
pprint.pprint(s1)


