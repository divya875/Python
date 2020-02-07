from bs4 import BeautifulSoup
import requests


def soup_search():
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")


    # pretty-printing
    # soup.prettify()

    # fetching title
    wikititle = soup.title
    print("Title is:", wikititle)

    # Writing results into a file
    with open("output1.html", "a") as file:
        file.write(str(wikititle))

    # fetching href's
    for links in soup.find_all('a'):
        hrefs = links.get('href')
        with open("output1.html", "a") as file:
            file.write(str(hrefs))
            file.write("\n")
        print(hrefs)


if __name__ == '__main__':
    soup_search()
