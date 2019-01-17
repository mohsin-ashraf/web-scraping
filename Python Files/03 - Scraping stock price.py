
# coding: utf-8

# In[1]:


#This time using mechanize instead of using urllib
import mechanize
#This time using lxml instead of using bs4 BeautifulSoup
import lxml.html
#time library is used to sleep between the requests that are made getting iteratively data from website
import time


# In[2]:


browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [("user-agent","Chrome")]


# In[3]:


url_to_apple_stock_value = "https://www.bloomberg.com/quote/AAPL:US"


# In[12]:


apple_html = browser.open(url_to_apple_stock_value)


# In[13]:


apple_html.code


# In[14]:


apple_html = apple_html.read()


# In[15]:


apple_html


# In[16]:


tree = lxml.html.fromstring(apple_html)


# In[17]:


price = tree.xpath('//span[@class="priceText__1853e8a5"]')


# In[18]:


price = price[0]
price.text_content()


# In[19]:


stock_price = float(price.text_content())
stock_price


# # Getting stock information iteratively

# In[20]:


for i in range(10):#You can put whatever number you want here...
    apple_html = browser.open(url_to_apple_stock_value).read()
    tree = lxml.html.fromstring(apple_html)
    price = tree.xpath('//span[@class="priceText__1853e8a5"]')
    price = price[0]
    print price.text_content()
    time.sleep(2)


# ### Requesting too many times to the same website in a very short time can block your ip address.
# <img src = 'imgs/mimitw.jpg'>
