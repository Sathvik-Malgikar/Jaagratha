from PIL import Image, ImageFont, ImageDraw
import datetime
import uuid


def create_cert(name, crime):

    id = str(uuid.uuid1())[0:20]

    raw = Image.open("./template.png").convert("RGB")
    im2=Image.open("../suspect.png")
    raw.paste(im2, (100, 400))
    # raw.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)
    # title_font =
    sub_font = ImageFont.truetype("./roboto.ttf", 20)
    date_font = ImageFont.truetype("./roboto.ttf", 60)
    editable = ImageDraw.Draw(raw)
    editable.text((500 - len(id) * 16, 190), id, (0, 0, 0), font=sub_font)
    editable.text((540, 190),  str(datetime.date.today()), (0, 0, 0), font=sub_font)
    editable.text((460 - len(name) * 16, 230), name, (0, 0, 0), font=sub_font)
    editable.text((730 - len("Jaagratha") * 16, 230), "Jaagratha", (0, 0, 0), font=sub_font)
    editable.text((460 - len(crime) * 16, 270), crime, (0, 0, 0), font=sub_font)
    # editable.text((1058 ,841),f"{offset} tons as of {datetime.date.today()}.",(40,40,40),font= sub_font)
    # editable.text((1678 ,841),str(activities),(25,25,25),font= sub_font)
    # editable.text((320 ,1020),f"{datetime.date.today()}",(25,25,25),font= date_font)
    raw.save(f"./{id}.png")


# create_cert("CCTV Dwarakanagar", "Arson")

