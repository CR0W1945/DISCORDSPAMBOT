import time
import requests
import pyfiglet

banner = pyfiglet.figlet_format("CR0W", font = "slant" )
print(banner)
spammsg = input("ur message u want send it ;-; : ")
wb = input("plz enter ur webhook url : ")
def work(spammsg, wb):
    while True:
        try:
            data = requests.post(wb, json={'content': spammsg})
            if data.status_code == 204:
                print(f"has been sent:  {spammsg}")
        except:
            print("webhooknotwork :" + wb)
            time.sleep(5)
            exit()
sleep = 1
while sleep == 1:
    work(spammsg, wb)
