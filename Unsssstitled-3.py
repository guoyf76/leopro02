def toggle_case(char):
    if char.isupper():
        return char.lower()
    else:
        return char.upper()

# 获取用户输入
input_char = input("请输入一个字母: ")

# 确保输入是一个字母
if len(input_char) == 1 and input_char.isalpha():
    # 转换大小写
    toggled_char = toggle_case(input_char)
    print(f"转换后的字母是: {toggled_char}")
else:
    print("请输入一个有效的字母。")