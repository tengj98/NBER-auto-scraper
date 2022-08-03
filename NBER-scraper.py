#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager


# In[5]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[6]:


driver.get("https://www.nber.org/papers")


# In[7]:


titles = driver.find_elements(By.CSS_SELECTOR, ".digest-card__title a")


# In[9]:


# Create new df
rows = []

for title in titles:
    row = {}
    row['title'] = title.text.strip()
    row['url'] = title.get_attribute("href")
    rows.append(row)


# In[10]:


df = pd.DataFrame(rows)


# In[11]:


df


# In[12]:


df.to_csv("nberresearch.csv",index=False)


# In[ ]:




