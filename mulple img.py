from requests import get
with open("img.txt", "r") as file:
    url_list = file.readlines()

i = 0
for url in url_list:
    url = url.strip("\n")
    res = get(url)

    with open(f"images/{i}.jpg","wb") as file:
        file.write(res.content)
    # i = i+1
    i +=1
