# 1. Please implement a string function in a numeric format in a language that you
# are good at. And mark every three digits with a comma. Please attach unit
# test.
# f(9527) => "9,527", f(3345678) => "3,345,678", f(-1234.45) => "-1,234.45"


def numeric_format(s):
    s = str(s)
    result = ""
    int_list = []
    if s[0:1] == "-":
        result += "-"
    is_decimal = s.find(".")
    if is_decimal != -1:
        n_decimal = s[is_decimal:]
    positive_int = abs(int(float(s)))
    while positive_int >= 1000:
        int_list.append(str(positive_int % 1000).zfill(3))
        positive_int = positive_int // 1000
    result += str(positive_int)
    if int_list:
        result += ","
    result += ",".join(int_list[::-1])
    if is_decimal != -1:
        result += n_decimal
    return result


if __name__ == '__main__':
    print(numeric_format(9527))
    print(numeric_format(3345678))
    print(numeric_format(-1234.45))
