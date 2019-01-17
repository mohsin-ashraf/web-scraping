
# coding: utf-8

# In[ ]:


#Setting up the script
import mechanize
import lxml.html
import urlparse
import csv


# In[ ]:


br = mechanize.Browser()#br short for browser
br.set_handle_robots(False)
br.addheaders = [("user-agent","Chrome")]


# In[ ]:


url = "https://www.pexels.com/search/sky/?page=1&format=js"


# In[ ]:


html_page = br.open(url).read()
tree = lxml.html.fromstring(html_page)


# In[ ]:


images = tree.cssselect('img')
len(images)


# In[ ]:


for image in images:
    try:
        print image.attrib['srcset']
    except KeyError: 
        continue
    #print "*"*100


# In[ ]:


url_string = "https://images.pexels.com/photos/912110/pexels-photo-912110.jpeg?auto=compress&cs=tinysrgb&h=350 1x, https://images.pexels.com/photos/912110/pexels-photo-912110.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=350 2x"
split_url = url_string.split('?')
split_url


# In[ ]:


split_url[0]


# In[ ]:


urls_to_images = []
for image in images:
    try:
        urls_to_images.append(image.attrib['srcset'].split('?')[0])
    except KeyError: 
        continue


# In[ ]:


len(urls_to_images)


# In[ ]:


#getting the extension of the image file maybe it's a jpeg,png or other type of image
type_of_image = urls_to_images[0]
type_of_image.split('.')
type_of_image


# In[ ]:


type_of_image = type_of_image.split('.')


# In[ ]:


type_of_image.reverse()
type_of_image[0]


# In[ ]:


for counter,url in enumerate(urls_to_images):
    type_of_image = url.split('.')[len(url.split('.'))-1]
    print type_of_image
    image = open('Data/Images/'+str(counter+1)+"."+type_of_image,"wb")
    image.write(br.open(url).read())
    image.close()


# In[ ]:


counter = 1
for page in range(1,15):
    url = "https://www.pexels.com/search/sky/?page="+str(page)+"&format=js"
    html_page = br.open(url).read()
    tree = lxml.html.fromstring(html_page)
    images = tree.cssselect('img')
    urls_to_images = []
    for image in images:
        try:
            urls_to_images.append(image.attrib['srcset'].split('?')[0])
        except KeyError: 
            continue
    #print len(urls_to_images)
    urls_to_images = [x.replace('\\\"',"") for x in urls_to_images]
    for url_to_img in urls_to_images:
        print url_to_img
        type_of_image = url_to_img.split('.')[len(url_to_img.split('.'))-1]
        image = open('Data/Images/sky_'+str(counter+1)+"."+type_of_image,"wb")
        image.write(br.open(url_to_img).read())
        image.close()

