from dhooks import Webhook, File, Embed
import os

os.system("cls")
print("""
Simple Embed Sender for Discord!
""")

whook = Webhook(input("webhook?: "))
desc = input("desc?: ")
embed = Embed(
    description = desc,
    timestamp='now'
    )
img1 = input("logo image link (imgur or anything): ")
image1 = img1
img2 = input("footer image link (imgur or anything): ")
image2 = img2
img3 = input("pfp image link (imgur or anything): ")

cname = input("author name?: ")
embed.set_author(name= cname, icon_url=img3)
askfield = input("add fields for reactions? (yes,no): ")
if askfield == "yes":
    fname1 = input("field name 1?: ")
    fval1 = input("field value 1?: ")
    embed.add_field(name=fname1, value=fval1)
    fname2 = input("field name 1?: ")
    fval2 = input("field value 1?: ")
    embed.add_field(name=fname2, value=fval2)
elif askfield == "no":
    pass
footerset = input("footer text?: ")
embed.set_footer(text=footerset, icon_url=img3)

embed.set_thumbnail(img1)
embed.set_image(img2)

whook.send(embed=embed)
