def convert_case(char):
    if len(char) != 1 or not char.isalpha():
        return "请输入单个字母"
    
    if char.islower():
        return char.upper()
    else:
        return char.lower()

if __name__ == "__main__":
    user_input = input("请输入一个字母：")
    result = convert_case(user_input)
    print(f"转换结果：{result}")
