import requests, re, json, os
from PIL import Image

URL         = "https://online.anyflip.com/icso/eprm/mobile/"
PDF_PATH    = "pdf.pdf"

if not os.path.exists(r'images'):
    os.makedirs(r'images' )

# request to the index page
res = requests.get(URL + "index.html", verify=False)

# extracting the config file id from the main request to the page
pattern = re.compile(r'javascript\/config\.js\?\d*')
config_id = pattern.findall(res.text)[0].split('?')[-1]

# get page list from config file
res = requests.get(URL + f"javascript/config.js?{config_id}", verify=False)
json_text = res.text.replace("var htmlConfig = ", '')[:-1]
json_file = json.loads(json_text)
page_count = json_file['meta']['pageCount']

# convert page_ids list to page_urls list
page_urls_list =[URL + f"../files/large/{page_id+1}.jpg" for page_id in range(page_count)]

# save each immage
for i, url in enumerate(page_urls_list):
    with open(f'images/image{i}.jpg', 'wb') as img:
        img.write(requests.get(url, verify=False).content)

# get image_paths list
image_paths_list = [Image.open(f"images/image{i}.jpg") for i in range(len(page_urls_list))]

image_paths_list[0].save(
    PDF_PATH, "PDF", resolution=100.0, save_all=True, append_images=image_paths_list[1:]
)