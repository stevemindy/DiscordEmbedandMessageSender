from dhooks import Webhook, File
import os

os.system("cls")
print("""
Simple Message Sender for Discord!
""")

webhook = Webhook(input("webhook?: "))
img = input("any image to send? (none = no yes = enter directory of file): ")
if img == "no":
    pass
    discord_pic = ''
else:
    discord_pic = File("images\\" + img)
text = input("what to send?: ")

if discord_pic == '':
    webhook.send(text)
else:
    webhook.send(text, file=discord_pic)
