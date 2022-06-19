from alright import WhatsApp



msg = msg = open('message.txt', 'r', encoding='utf-8-sig').read()

messenger = WhatsApp()
# messenger.find_user('972509931102')
with open('1.csv') as f:
    numbers = f.read().splitlines()

for number in numbers:
    messenger.send_message1(number, msg)

