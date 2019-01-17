
# coding: utf-8

# In[1]:


#Setting up the script
import mechanize
import lxml.html
import urlparse
import csv


# In[2]:


url = "https://www.daraz.pk/catalog/?q=computer&page="#number will be placed accordingly


# In[3]:


br = mechanize.Browser()#br short for browser
br.set_handle_robots(False)
br.addheaders = [("user-agent","Chrome")]


# In[4]:


#Here I am using hard coded url just for quick first page scraping illustration
html_page = br.open('https://www.daraz.pk/catalog/?q=computer')
html_page.code


# In[5]:


html_page = html_page.read()


# In[6]:


tree = lxml.html.fromstring(html_page)


# In[7]:


items = tree.cssselect('a.link')


# In[8]:


len(items)


# In[9]:


images = []
for i in items:
    image = i.cssselect('img')
    image = image[0]
    link_to_image = image.attrib['data-src']
    print link_to_image
    images.append(link_to_image)
len(images)


# In[13]:


altname = []
for i in items:
    image = i.cssselect('img')
    image = image[0]
    name = image.attrib['alt']
    print name
    altname.append(name)
len(images)


# In[16]:


xpath = '//section[@class="products"]//a//span[@class="name"]'
item_names = tree.xpath(xpath)
len(item_names)


# In[18]:


item_names = [x.text_content() for x in item_names]


# In[20]:


for i in item_names:
    print i


# In[21]:


xpath = '//section[@class="products"]//a//div[@class="price-container clearfix"]//span[@class="price-box ri"]'
prices_of_items = tree.xpath(xpath)
prices = []
len(prices_of_items)
for i in prices_of_items:
    prices.append(i.cssselect('span')[1].text_content().replace('Rs','').replace('.',''))
len(prices)


# In[22]:


for i in prices:
    print i.strip()


# In[24]:


def safeStr(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    except: return ""


# In[26]:


csv_file = open('daraz.pk.csv','wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product Name","Product Price","Product Image"])
for name,price,img in zip(item_names,prices,images):
    csv_writer.writerow([safeStr(name),safeStr(price),safeStr(img)])
csv_file.close()


# In[27]:


csv_file = open('Data/daraz.pk.csv','wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product Name","Product Price","Product Image"])
for name,price,img in zip(item_names,prices,images):
    csv_writer.writerow([safeStr(name),safeStr(price),safeStr(img)])
csv_file.close()


# In[28]:


links_to_item_detail = []
for i in items:
    links_to_item_detail.append(i.attrib['href'])
len(links_to_item_detail)


# In[29]:


for i in links_to_item_detail:
    print i


# In[35]:


features = []
for counter , url in enumerate(links_to_item_detail):
    if counter == 5:
        break
    page = br.open(url).read()
    tree = lxml.html.fromstring(page)
    key_features = tree.xpath('//div[@class="list -features -compact -no-float"]')
    key_features = key_features[0]
    key_features_list = key_features.cssselect('li')
    product_features = []
    for feature in key_features_list:
        product_features.append(feature.text_content().strip())
        print feature.text_content().strip()
    print "*"*120


# # You can write all of these features to csv file as well but I am not going to do that here
