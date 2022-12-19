from requests import get
file = open("img.txt", 'r+')
img_url_list =  file.readlines()
file.close()
new_url = []
for url in img_url_list:
    url_list = url.strip("\n")
    new_url .append(url_list)

single_url = new_url[0]
res = get(single_url)

with open("sumon.jpg", "wb") as file:
    file.write(res.content)