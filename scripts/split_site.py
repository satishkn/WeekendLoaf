import re, os

html = open('index_extracted.html','r',encoding='utf8').read()
# capture head and nav separately
style = re.search(r'<style>.*?</style>', html, flags=re.DOTALL).group(0)
meta_title = re.findall(r'<meta[^>]+>|<title>.*?</title>', html)
head = ''.join(meta_title) + style
# extract nav
nav = re.search(r'<nav.*?</nav>', html, flags=re.DOTALL).group(0)
# update nav links
nav = nav.replace('href=#hero','href="index.html"')
nav = nav.replace('href=#story','href="about.html"')
nav = nav.replace('href=#product','href="products.html"')
nav = nav.replace('href=#order','href="about.html"')
nav = nav.replace('href=#contact','href="contact.html"')

# function to get section by id

def get_section(id):
    m = re.search(r'<section[^>]*id="?'+id+'"?[^>]*>.*?</section>', html, flags=re.DOTALL)
    return m.group(0) if m else ''

hero = get_section('hero')
story = get_section('story')
product = get_section('product')
order = get_section('order')
contact = re.search(r'<footer[^>]*id="?contact"?[^>]*>.*?</footer>', html, flags=re.DOTALL).group(0)

# extra section "Bread worth waiting for"
extra = ''
match = re.search(r'<section[^>]*>\s*<div[^>]*>\s*<span[^>]*>Why Weekend Loaf</span>.*?</section>', html, flags=re.DOTALL)
if match:
    extra = match.group(0)

# testimonial section
test = ''
match2 = re.search(r'<section[^>]*>\s*<div[^>]*>\s*<span[^>]*>Happy Customers</span>.*?</section>', html, flags=re.DOTALL)
if match2:
    test = match2.group(0)

os.makedirs('pages',exist_ok=True)

def write(fname, body):
    with open(fname,'w',encoding='utf8') as f:
        f.write('<!DOCTYPE html><html lang="en"><head>'+head+'</head><body>')
        f.write(nav)
        f.write('<main>'+body+'</main>')
        if fname!='pages/contact.html':
            f.write(contact)
        f.write('</body></html>')

index_body = hero + '<section class="py-8 text-center"><a href="products.html" class="font-bold underline">View our product</a> | <a href="about.html" class="font-bold underline">Our Story</a></section>'
write('index.html', index_body)

about_body = story + order + extra + test
write('pages/about.html', about_body)

products_body = product + extra
write('pages/products.html', products_body)

write('pages/contact.html', contact)

print('pages generated')
