
# coding: utf-8

# # Scrapping your very first website 
# # <h1 style ='color:green'>projecteuler.net</h1> 

# In[25]:


#just to handle some wierd charactors
def safeStr(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    except: return ""


# In[2]:


import urllib
from bs4 import BeautifulSoup
import urlparse


# In[3]:


projecteuler_url = "https://projecteuler.net/archives"


# In[4]:


html = urllib.urlopen(projecteuler_url)


# In[6]:


html.code 


# ### Status code 200 means every thing is good to go

# In[7]:


html = html.read()


# In[9]:


html


# In[10]:


soup = BeautifulSoup(html,'html.parser')


# In[11]:


table = soup.select('table#problems_table')


# In[12]:


print table


# In[13]:


len(table)


# In[14]:


table = table[0]


# In[15]:


table


# In[16]:


type(table)


# In[17]:


table_rows = table.find_all('tr')
len(table_rows)


# In[18]:


for i in table_rows:
    for j in i.find_all('td'):
        print str(j.text).ljust(50),
    print 


# In[19]:


# Getting urls to problems
links = table.find_all('a')
len(links)


# In[20]:


for i in links:
    print i.attrs['href']


# In[21]:


#Converting the relative urls to absolute urls
for i in links:
    print urlparse.urljoin(projecteuler_url,i.attrs['href'])


# In[22]:


project_euler_problem_3 = urllib.urlopen('https://projecteuler.net/problem=3').read()
project_euler_problem_3


# In[23]:


soup = BeautifulSoup(project_euler_problem_3,'html.parser')
problem_content = soup.select('div.problem_content')
problem_content


# In[24]:


problem_content = problem_content[0]
for p in problem_content.select('p'):
    print p.text

