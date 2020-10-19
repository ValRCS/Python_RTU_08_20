#!/usr/bin/env python
# coding: utf-8




from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[2]:


browser = webdriver.Firefox()


# In[3]:


browser.get('http://www.ss.com')
assert 'SS' in browser.title


# In[ ]:


# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)


# In[4]:


browser.current_url


# In[5]:


cars =browser.find_element_by_id("mtd_97")
type(cars)


# In[6]:


cars.get_attribute('href')


# In[7]:


cars.get_attribute('title')


# In[8]:


cars.text


# In[9]:


# https://devhints.io/xpath
apart = browser.find_element_by_xpath('//a[@title="Dzīvokļi"]') # XPath is very powerful tool for finding elements


# In[11]:


apart.click() # i can emulate a mouse click


# In[12]:


browser.back()


# In[14]:


browser.forward()


# In[15]:


riga = browser.find_element_by_xpath('//a[@title="Rīga, Sludinājumi"]')
type(riga)


# In[16]:


riga.click()


# In[ ]:


myel = browser.find_element_by_id()


# In[17]:


browser.current_url


# In[19]:


browser.get_window_size()


# In[21]:


# save with Pillow graphibrowser.get_screenshot_as_png()


# In[22]:


browser.save_screenshot("page.png")

