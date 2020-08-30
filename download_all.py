import requests
import bs4
import os
import urllib.parse

download_base_url = "https://thetrove.net/Books/Twilight%202000/Merc%202000/"
out_file_path = "C:/Users/kreegan/Downloads/bulk"
download_file_extension = ".pdf"

sess = requests.Session()

# Load base page to ensure it's up
response = sess.get(download_base_url)
response.raise_for_status()

# print("Initial load response : ", response.text)

parsed = bs4.BeautifulSoup(response.text, "html.parser")
parsed.prettify()

links = parsed.find_all("a")
print("Just the links:")
for link in links:
    if "href" in link.attrs:
        if download_file_extension in link["href"]:
            print("Link href : ", link.attrs["href"][2:])
            if "http" in link.attrs["href"]:
                download_path = link.attrs["href"]
            else:
                download_path = f"" + download_base_url + link.attrs["href"][2:]
            print("Download path : ", download_path)
            file_name = f"" + os.path.join(out_file_path, download_path.split("/")[-1])
            file_name = urllib.parse.unquote(file_name).replace("?", "")
            print("File name : ", file_name)

            with sess.get(download_path, stream=True) as link_response:
                link_response.raise_for_status()
                file_size = int(link_response.headers.get("Content-Length", 0))
                print("Link response : ", link_response)
                print("File size : ", file_size)
                with open(file_name, "wb") as file:
                    for chunk in link_response.iter_content(8192):
                        file.write(chunk)


