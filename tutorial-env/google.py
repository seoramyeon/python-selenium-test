from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.daum.net/')
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
