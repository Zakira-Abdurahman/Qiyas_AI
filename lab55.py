from bs4 import BeautifulSoup

#exercise 1

html = """
<html>
<body>
<h1> Python Web Scraping </h1>
</body>
</html> 
"""

soup = BeautifulSoup(html, 'html.parser') #create a BeautifulSoup object by parsing the HTML string
print(soup) #print the entire HTML
print(soup.h1) #print the h1 tag
print(soup.h1.string) #print the text inside the h1 tag

heading = soup.find('h1') #find the h1 tag
print(heading) #print the h1 tag
print(heading.string) #print the text inside the h1 tag


#exercise 2
html = """
<html>
<body>
<p>Python</p>
<p>Java</p>
<p>C++</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser') #create a BeautifulSoup object by parsing the HTML string
paragraph = soup.find("p") #find the first p tag
print(paragraph) #print the first p tag
paragraphs = soup.find_all("p") #find all p tags
print(paragraphs) #print all p tags

#exercise 3
html = """
<html>
<body>
<li>Python</li>
<li>Java</li>
<li>C#</li>
<li>Go</li>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser') #create a BeautifulSoup object by parsing the HTML string
items = soup.find_all("li") #find all li tags
print(items) #print all li tags
for item in items:
    print(item.string) #print the text inside each li tag

#exercise 4
html = """
<a href="https://google.com">Google</a>
<a href="https://facebook.com">Facebook</a>
<a href="https://twitter.com">Twitter</a>
"""

soup = BeautifulSoup(html, 'html.parser') #create a BeautifulSoup object by parsing the HTML string
links = soup.find_all("a") #find all a tags
for link in links:
    print(link["href"]) #print the href attribute of each a tag


#exercise 5
html = """
<div class="product"> Iphone</div>
<div class="product"> Macbook</div>
<div class="product"> Ipad</div>
"""
soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all(class_ = "product") #find all div tags with class "product"
print(products) #print all div tags with class "product"
for product in products:
    print(product.string) #print the text inside each div tag with class "product"


# exercise 6
html = """
<html>
<body>
<div class ="news">
<h2> <a href="https://site.com/a">AI is growing fast</a></h2>
</div>
<div class="news">
<h2><a href="https://site.com/b">Python is everywhere</a></h2>
</div>
<div class="news">
<h2><a href="https://site.com/c">Tech jobs in 2026</a></h2>
</div>
</body>
</html>
"""
soup= BeautifulSoup(html, "html.parser")
news_block = soup.find_all("div", class_="news")
for block in news_block:
    title = block.h2.a.string
    link = block.h2.a["href"]
    print("Title:", title)
    print("link", link)
    

# exercise7
html = """
<html>
<body>
<div class="product">
<h3>iphone 15 </h3>
<span class="price">$999</span>
</div>
<div class="product">
<h3>Macbook air</h3>
<span class="price">$997</span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="product")
for p in products:
    name = p.find("h3").text
    price = p.find("span", class_="price").text
    print(f"{name} -> {price}")


# exercise8
html ="""
<html>
<body>
<nav>
<a href="/home">home</a>
<a href="/about">about</a>
<a href="/contact>contact</a>
</nav>
</body>
</html>

"""

soup = BeautifulSoup(html, "html.parser")
links=soup.find_all("a")
for l in links:
    print(l.text,"->", l["href"])
    
# exercise9
html ="""
<ul>
<li>python</li>
<li>java</li>
<li>python for ai</li>
<li>c++</li>
</ul>

"""


soup= BeautifulSoup(html, "html.parser")
items = soup.find_all("li")
for item in items:
    if "python" in item.text:
        print("found:", item.text)


# exercise10

html = """
<p> contact us at: info@gmail.com</p>
<p>support: support@company.com</p>
"""

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
words = text.split()
for word in words:
    if "@" in word:
        print("email:", word)
        
        