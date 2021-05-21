from module.adapter import pack_info

# 测试中英文的分段
str_e = "this is a sentence"
str_ch = "这是一句中文"
str_all = "this is sentence and \n this is also interesting 这里也有中文"
str_need = ''
for ch in str_all:
    if ord(ch) not in range(0, 127):
        break
    if ch != '\n':
        str_need = str_need + ch
    else:
        str_need = str_need + ' '
# print(str_need)

str = "this\n\n is\n an \nexample\n"
print(str)
print(str.replace('\n', ' '))

test = [1]
print(type(test))
print(test)
if len(test) != 0:
    print("test is not null")
