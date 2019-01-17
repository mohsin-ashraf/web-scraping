
# coding: utf-8

# #  <h1 style='text-align:center'> The three ways of print </h1>

# In[21]:


print "Hello World!\n"
print 'Hello World!\n'
print """Hello
World!
    """


# # Python supports dynamic typing so you dont have to specify the type of the variables

# In[2]:


var_1 = 'String variable'
var_2 = 1213
var_3 = 312.321312
var_4 = 3+9j
var_5 = 'a'
print var_1
print var_2
print var_3
print var_4
print var_5


# # Types of the variables can be changed at any moment

# In[3]:


var_1 = 312312
var_2 = 'afdsffasd'
print var_1
print var_2


# # Loops 

# In[5]:


#Basic for loop
for i in range(10):
    print i

#the above code is quite similer to the following C++ code
#    for (int i =0 ; i < 10 ; i++)
#        cout <<i<<endl;


# In[6]:


start = 1
end = 15
step = 2
for i in range(start,end,step):
    print i


# In[7]:


number = 1
while number < 10:
    print number
    number+=1 #there is no ++ operator in python as C++ or java have use += instead


# # Conditional Statements

# In[25]:


number = 10
if number == 5:
    print "This block will not execute"
elif number == 7:
    print "Nothing io gonna happen"
#you can put as many elif as you want
elif number == 10:
    print "Yes the number is equal to ",number
else:
    print "I will take care of the rest"


# # Lists (Arrays)

# In[8]:


empty_array = []
filled_array = [1,2,3,4,5,6,7,8,9]
# filling numbers in empty_array
for i in range(10):
    empty_array.append(i+1)
print "Elements in empty array : ",empty_array
print "Elements in filled_array : ",filled_array


# In[21]:


#iterating through the list
size_of_array = len(empty_array)
for i in range(size_of_array):
    print empty_array[i],


# In[22]:


#Example of forEach loop in python
for i in empty_array:
    print i,


# In[11]:


#two D arrays
two_d_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print two_d_array


# In[17]:


for i in two_d_array:
    for j in i:
        print str(j).center(5,' '),
    print 


# In[20]:


initial_sized_array = [0]*1000
print len(initial_sized_array)


# # Functions

# In[23]:


# Functions do not need the return type or the types of perameters that we are going to pass 
def add(a,b):
    return a+b
print add(10,20)


# In[24]:


#Implicite return is None
def void_function():
    pass#just pass do nothing
a = void_function()
print a


# In[2]:


string = "Hi I'm a string"


# In[3]:


print string.upper()


# In[4]:


print string.lower()


# In[5]:


print string.title()


# In[8]:


print string.replace('string','very good string')


# In[10]:


#Orignal string is still the same as it was initially created.
print string


# In[11]:


print string.find("string")


# In[12]:


print string.find('This is not in the string')


# In[13]:


print string.isdigit()


# In[14]:


string += ' 434'
print string.find('434')


# In[15]:


print string


# In[18]:


print string[16:19]


# In[19]:


print string[16:19].isdigit()

