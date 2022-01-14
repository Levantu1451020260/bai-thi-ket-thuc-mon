name = input("nhập tên đệm:")
print("Tên đệm:",name)
def tongcacso(n):
    M = 0;
    while (n > 0):
        M = M + n % 10;
        n = int(n / 10);
    return M;
n = int(input("Nhập số n = "));
print("Tổng của", n, "là", tongcacso(n));