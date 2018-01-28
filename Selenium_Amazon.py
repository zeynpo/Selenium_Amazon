from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox ()
driver.maximize_window ()
driver.get ("https://www.amazon.com")

#sayfanın tam yüklenmesi için zaman verdim
time.sleep(10)


sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[4]/div[3]/div[2]/div/div[1]/div/a/span")

time.sleep(8)

# //*[@id="ap_email"]
# //*[@id="ap_password"]

email = driver.find_element_by_xpath ("//*[@id='ap_email']")
password = driver.find_element_by_xpath ("//*[@id='ap_password']")

email.send_keys("zeynep.ocakci@hotmail.com")
password.send_keys("zeynep95@amazon")

time.sleep(6)

signing = driver.find_element_by_xpath ("//*[@id='signInSubmit']")
singing.click()
time.sleep(6)


search = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
search.send_keys("samsung")
searching = driver.find_element_by_xpath ("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
searching.click()
time.sleep(6)
# 
secondpage = driver.find_element_by_xpath ("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[5]/div/div/span[3]/a")
secondpage.click()
time.sleep(5)

# //*[@id="result_2"] 3.result'a assign edilen id budur. Sıfırdan başlıyor.
thirdresult =driver.find_element_by_xpath ("//*[@id='result_2']")
time.sleep(5)


clickproduct = driver.find_element_by_xpath ("/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[3]/div/div/div/div[2]/div[1]/div[1]/a/h2")
clickproduct.click()
time.sleep(5)

addtolist = driver.find_element_by_name ("submit.add-to-registry.wishlist")
time.sleep(5)

wishlist = driver.find_element_by_xpath ("/html/body/div[6]/div/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div/span/div/label/i")
wishlist.click()
time.sleep(5)

createlist = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/form/div[2]/span[3]/span/span/input")
createlist.click()
time.sleep(5)

confirmlist = driver.find_element_by_xpath ("/html/body/div[6]/div/div/div[2]/div[2]/div[3]/div/div[2]/span[1]/span/a")
confirmlist.click()
time.sleep(5)

deleteproduct = driver.find_element_by_name ("submit.deleteItem")
deleteproduct.click()
time.sleep(5)

# listenin boş olduğunu onayla
confirmdeleting = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[1]/a")
confirmdeleting.click()
time.sleep(8)

driver.close ()




















