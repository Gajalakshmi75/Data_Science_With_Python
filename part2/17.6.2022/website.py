page='welcome <a href="https://WWW.YAHOOO.COM">HELLO HOW ARE YOU'
print(page)
def getURL(page):
    start_link=page.find("<a href")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]
    return url
url=getURL(page)
print(url)
