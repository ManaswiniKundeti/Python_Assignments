from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
attr = soup.find("h3")["data-example"]
print(attr)


# el = soup.select(".special")[0]
# print(el)
# print(el.get_text())  #prints only the text in the element
# for el in soup.select(".special"):
#   print(el.name)
#   print(el.attrs['class']) #we are only selecting things with class special
#   # print(el.get_text())  #prints all the text with class special