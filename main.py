import os
import codecs
from markdownify import markdownify as md
from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#The%20basic%20find%20method:%20findAll(name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs)


def getHtmlContent(var_name=""):
    return '<b>yoto</b> <a href="http://github.com">%s</a>' % var_name

def getHtmlFromFile(file):
    # return codecs.open(file, 'r', 'utf-8')
    text = ""
    try:
        with open(file, "r", encoding='utf-8') as f:
            text= f.read()
    except ex:
        pass
    return text

# html_content = getHtmlContent("example md proj")


def mdGenerator(fileName, fileLocation):
    file_name = fileName.replace('.html', '')
    print(file_name, fileLocation)

    file_path = os.path.join(os.getcwd(), 'source', '%s.html' % file_name)
    html_content = getHtmlFromFile(fileLocation)
    soup = BeautifulSoup(html_content, "html.parser")

    md_file = os.path.join(os.getcwd(), 'md', "%s.md" % file_name)
    with open(md_file, 'w') as f:
        # title
        f.write("# %s" % soup.h1.text.strip())
        f.write("\n")
        f.write("## Full Description")
        f.write("\n")
        
        # description
        f.write("%s" % soup.findAll(attrs={'class' : 'uk-width-medium-1-1'})[11].text.strip())
        f.write("\n")

source_dir = os.path.join(os.getcwd(), 'source')
for r, d, f in os.walk(source_dir):
    for file in f:
        if not ".html" in file: continue
        mdGenerator(file, os.path.join(r, file))