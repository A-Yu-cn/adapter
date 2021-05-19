from module.adapter import split_str
from module.adapter import pack_info

# 测试中英文的分段
str_e = "this is a sentence"
str_ch = "这是一句中文"
str_all = "this is sentence and 这里也有中文"
str_need = ''
for ch in str_all:
    if ord(ch) not in range(0, 127):
        break
    str_need = str_need + ch

if __name__ == "__main__":
    s = input("请随意输入一句话:\n")
    res = split_str(s)
    print(pack_info(res))
