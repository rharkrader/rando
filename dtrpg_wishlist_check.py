import requests
import bs4

dtrpg_base_url = "https://www.drivethrurpg.com"
login_path = dtrpg_base_url + "/login.php"
validate_login_path = dtrpg_base_url + "/validate_login.php"
validate_credentials_path = dtrpg_base_url + "/validate_credentials.php"
wishlist_path = dtrpg_base_url + "/wishlist.php"
username = "rharkrader@gmail.com"
password = "ftTvLm7ESFnKfY!"
out_file_path = "./output.html"

sess = requests.Session()

# Load base page to ensure it's up
response = sess.get(dtrpg_base_url)
response.raise_for_status()

# Login to my account
val_cred_data = {
    "action": "process",
    "origin": "returning_customer_popup",
    "checkout_after_login": "0",
    "redirect_url": "/",
    "remember_me": "",
    "field-form-id": "login",
    "field-form-time": "1560453214",
    "field-form-token": "69b3ba226bb8460fc50dec9c229c262f",
    "field-form-ajax": "",
    "field-form-ajax-id": "",
    "email_address": username,
    "password": password
}
login_response = sess.post(login_path, val_cred_data)
login_response.raise_for_status()
# print("Login response : ", login_response.text)

if "Log Off" not in login_response.text:
    print("LOGIN UNSUCCESSFUL!!!")
    exit(-1)

# Load wishlist
wishlist_response = sess.get(wishlist_path)
# print("Wishlist response: " + wishlist_response.text)

parsed = bs4.BeautifulSoup(wishlist_response.text, "html.parser")
parsed.prettify()

out_file = open(out_file_path, "w")
out_file.write("<html><head></head><body>")
spans = parsed.find_all("span")
# print("Just the spans:")
for span in spans:
    if "class" in span.attrs:
        if "wish-price-special" in span["class"]:
            out_file.write(str(span.parent))
            # print(span.parent)
out_file.write("</body></html>")
out_file.close()

links = parsed.find_all("a")
print("Just the links:")
for link in links:
    if "href" in link.attrs:
        if "/product/" in link["href"]:
            print(link.attrs["href"])
            print(link.text)

