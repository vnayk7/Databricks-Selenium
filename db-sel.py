# Databricks notebook source
# Getting Selenium
%pip install selenium

# COMMAND ----------

# MAGIC %sh
# MAGIC wget https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip -O /tmp/chromedriver_linux64.zip
# MAGIC

# COMMAND ----------

# MAGIC %sh 
# MAGIC mkdir -p /tmp/chromedriver
# MAGIC unzip /tmp/chromedriver_linux64.zip -d /tmp/chromedriver/

# COMMAND ----------

# MAGIC
# MAGIC %sh
# MAGIC sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
# MAGIC sudo echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
# MAGIC sudo apt-get -y update
# MAGIC sudo apt-get -y install google-chrome-stable
# MAGIC # /usr/bin/yes | sudo apt install google-chrome-stable chromium-chromedriver
# MAGIC

# COMMAND ----------

pip install webdriver-manager

# COMMAND ----------

pip list


# COMMAND ----------



# COMMAND ----------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = Options()

options.add_argument("--no-sandbox")

options.add_argument("--headless")

options.add_argument("--disable-dev-shm-usage")

options.add_argument('--window-size=1920,1480')
options.add_argument('--start-maximised')
options.add_argument("--remote-debugging-port=9009")
# options.add_experimental_option("prefs", {
#   "download.default_directory": r"/dbfs/dl_zi",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })
# prefs = {'download.default_directory' : '/dbfs/dl_zi/'}
# options.add_experimental_option('prefs', prefs)
print(f"Launching Chrome...")

chrome_driver = "/tmp/chromedriver/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print(f"Chrome launched.")


# COMMAND ----------

driver.get("https://zoominfo.app.box.com/s/c702utzg68zwxm5brh4br54f9g1g654w/folder/178243238782")


# COMMAND ----------

driver.find_element(By.CLASS_NAME,value="ItemListBreadcrumb-currentItemTitle.page-title").text

# COMMAND ----------

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium.webdriver.support.ui import Select
import os

# Function to check if current download process has finished or not 
def wait_for_download_to_finish():
            import time
            print("Waiting for download to start", end="")
            time.sleep(20)
            while any([filename.endswith(".crdownload") for filename in 
               os.listdir("/databricks/driver/")]):
                time.sleep(20)
                print(".", end="")
            print("done!")
# Code to loop over the pages,select all files on the page and download them    
for index in range(5, 51):
        base_url="https://zoominfo.app.box.com/s/c702utzg68zwxm5brh4br54f9g1g654w/folder/178243238782?page="
        url=base_url+str(index)
        print(url)
        driver.get(url)
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        name=driver.find_element(By.CLASS_NAME,value="sort-label")
        webdriver.ActionChains(driver).move_to_element(name).context_click(name)
        webdriver.ActionChains(driver).context_click(name).perform()
        menuitem=driver.find_element(By.CLASS_NAME,value="menu-item")
        driver.execute_script("arguments[0].click();", menuitem)
        wait_for_download_to_finish()
        # renaming the file that was downloaded for current page
        os.rename("ZI_COMP_WITH_ADDITIONAL_INSIGHTS_WITH_LINKAGES_20221001-selected.zip","/databricks/driver/set_"+str(index)+".zip")
        dbutils.fs.mv("file:///databricks/driver/set_"+str(index)+".zip","dbfs:/path",True)
        

# COMMAND ----------

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium.webdriver.support.ui import Select
import os

# Function to check if current download process has finished or not 
def wait_for_download_to_finish():
            import time
            print("Waiting for download to start", end="")
            time.sleep(20)
            while any([filename.endswith(".crdownload") for filename in 
               os.listdir("/databricks/driver/")]):
                time.sleep(20)
                print(".", end="")
            print("done!")
# Code to loop over the pages,select all files on the page and download them    
for index in range(19, 51):
        base_url="https://zoominfo.app.box.com/s/c702utzg68zwxm5brh4br54f9g1g654w/folder/178243238782?page="
        url=base_url+str(index)
        print(url)
        driver.get(url)
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        name=driver.find_element(By.CLASS_NAME,value="sort-label")
        webdriver.ActionChains(driver).move_to_element(name).context_click(name)
        webdriver.ActionChains(driver).context_click(name).perform()
        menuitem=driver.find_element(By.CLASS_NAME,value="menu-item")
        driver.execute_script("arguments[0].click();", menuitem)
        wait_for_download_to_finish()
        # renaming the file that was downloaded for current page
        os.rename("ZI_COMP_WITH_ADDITIONAL_INSIGHTS_WITH_LINKAGES_20221001-selected.zip","/databricks/driver/set_"+str(index)+".zip")
        dbutils.fs.mv("file:///databricks/driver/set_"+str(index)+".zip","dbfs:/path",True)
        


# COMMAND ----------

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium.webdriver.support.ui import Select
import os

# Function to check if current download process has finished or not 
def wait_for_download_to_finish():
            import time
            print("Waiting for download to start", end="")
            time.sleep(20)
            while any([filename.endswith(".crdownload") for filename in 
               os.listdir("/databricks/driver/")]):
                time.sleep(20)
                print(".", end="")
            print("done!")
# Code to loop over the pages,select all files on the page and download them    
for index in range(23, 51):
        base_url="https://zoominfo.app.box.com/s/c702utzg68zwxm5brh4br54f9g1g654w/folder/178243238782?page="
        url=base_url+str(index)
        print(url)
        driver.get(url)
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        name=driver.find_element(By.CLASS_NAME,value="sort-label")
        webdriver.ActionChains(driver).move_to_element(name).context_click(name)
        webdriver.ActionChains(driver).context_click(name).perform()
        menuitem=driver.find_element(By.CLASS_NAME,value="menu-item")
        driver.execute_script("arguments[0].click();", menuitem)
        wait_for_download_to_finish()
        # renaming the file that was downloaded for current page
        os.rename("ZI_COMP_WITH_ADDITIONAL_INSIGHTS_WITH_LINKAGES_20221001-selected.zip","/databricks/driver/set_"+str(index)+".zip")
        dbutils.fs.mv("file:///databricks/driver/set_"+str(index)+".zip","dbfs:/path",True)

# COMMAND ----------

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium.webdriver.support.ui import Select
import os

# Function to check if current download process has finished or not 
def wait_for_download_to_finish():
            import time
            print("Waiting for download to start", end="")
            time.sleep(20)
            while any([filename.endswith(".crdownload") for filename in 
               os.listdir("/databricks/driver/")]):
                time.sleep(20)
                print(".", end="")
            print("done!")
# Code to loop over the pages,select all files on the page and download them
index=28    
base_url="https://zoominfo.app.box.com/s/c702utzg68zwxm5brh4br54f9g1g654w/folder/178243238782?page="
url=base_url+str(index)
print(url)
driver.get(url)
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
name=driver.find_element(By.CLASS_NAME,value="sort-label")
webdriver.ActionChains(driver).move_to_element(name).context_click(name)
webdriver.ActionChains(driver).context_click(name).perform()
menuitem=driver.find_element(By.CLASS_NAME,value="menu-item")
driver.execute_script("arguments[0].click();", menuitem)
wait_for_download_to_finish()
# renaming the file that was downloaded for current page
os.rename("ZI_COMP_WITH_ADDITIONAL_INSIGHTS_WITH_LINKAGES_20221001-selected.zip","/databricks/driver/set_"+str(index)+".zip")
dbutils.fs.mv("file:///databricks/driver/set_"+str(index)+".zip","dbfs:/path",True)

# COMMAND ----------

# MAGIC %sh 
# MAGIC  ps -ef | grep chrome 
# MAGIC # kill -9 22526
# MAGIC # ls -al -h ./
# MAGIC # pwd
# MAGIC

# COMMAND ----------


dl=driver.find_element(By.CLASS_NAME,value="SharedFolderActionBar-download")

driver.execute_script("arguments[0].click();", dl)






