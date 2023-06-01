import webbrowser
from urllib.error import URLError

def get_user_url():
    user_url = input("Enter a URL: ")
    return user_url

def check_url(user_url):
    if user_url.endswith(".pl") or user_url.endswith(".com"):
        if user_url.startswith("http://") or user_url.startswith("https://"):
            return True
        else:
            user_url = "http://" + user_url
            return user_url
    else:
        raise URLError("Invalid URL")
       # return False

def main():
    user_url = get_user_url()
    try:
        user_url =  check_url(user_url)
    except URLError:
        print("Invalid URL")
    webbrowser.open(user_url)

if __name__ == "__main__":
    main()