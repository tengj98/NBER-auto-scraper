#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd


# In[3]:


from bs4 import BeautifulSoup


# In[5]:


response = requests.get("https://www.nber.org/papers")
doc = BeautifulSoup(response.text)


# In[6]:


doc


# In[99]:


import pandas as pd

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager


# In[100]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[101]:


driver.get("https://www.nber.org/papers")


# In[102]:


titles = driver.find_elements(By.CSS_SELECTOR, ".digest-card__title a")


# In[103]:


summary = driver.find_elements(By.CSS_SELECTOR, ".digest-card__summary")


# In[108]:


# Create new df
rows = []

for title in titles:
    row = {}
    row['title'] = title.text.strip()
    row['url'] = title.get_attribute("href")
    rows.append(row)


# In[109]:


df = pd.DataFrame(rows)


# In[110]:


df


# In[82]:


df.to_csv("nberresearch.csv",index=False)


# In[ ]:




