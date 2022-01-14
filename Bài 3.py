name = input("nhập Tên:")
print("Họ Và Tên:",name)
def kiemtrathuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;
n = int(input("Nhập n = "));
print("số nguyên", n, "là:", kiemtrathuannghich(n));