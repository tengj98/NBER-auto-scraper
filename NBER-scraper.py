#!/usr/bin/env python
# coding: utf-8

# In[1]:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

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




