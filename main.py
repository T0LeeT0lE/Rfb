import requests

def report_facebook_account(link, count):
    for _ in range(count):
        response = requests.post(link, data={"report": "spam"})
        if response.status_code == 200:
            print("Report berhasil dikirim.")
        else:
            print("Gagal mengirim report.")

# Ganti dengan tautan yang sesuai
tautan = "https://www.facebook.com/share/155Fzeg2W9/"
report_facebook_account(tautan, 100)

