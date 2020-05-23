def dup_str_n_times(t: int):
    def dup_str(s: str):
        return s * t
    return dup_str


dup_3 = dup_str_n_times(3)
dup_2 = dup_str_n_times(2)

print(dup_2('aaa'))
print(dup_3('b'))
