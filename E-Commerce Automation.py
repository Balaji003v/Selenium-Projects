from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#- Launch Chrome browser using Selenium WebDriver
driver = webdriver.Chrome()

#- Open the Angular practice site
driver.get("https://rahulshettyacademy.com/angularpractice/")

#- Set an implicit wait to handle dynamic elements
driver.implicitly_wait(5)

#Click on the link that navigates to the shop section
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()

#- Find all product cards on the shop page using XPath
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products :

    #- Extract the product name using relative XPath and through the.text
    productName = product.find_element(By.XPATH,"div/h4/a").text

    #- If the product name matches "Blackberry":
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()


driver.find_element(By.CSS_SELECTOR,"a[class*='btn btn-primary']").click()

# Click the "Add to Cart" button inside that product card
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

#- Type "ind" into the country input field
driver.find_element(By.ID,"country").send_keys("ind")

#- Wait explicitly until the suggestion "India" appears.
wait = WebDriverWait(driver,10)

# wait until India Shows on the dropdown menu
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

#- Click on "India" from the dropdown
driver.find_element(By.LINK_TEXT,"India").click()

#- Click the checkbox to agree to terms and conditions
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

#- Click the submit button to place the order.
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()

#- Capture the success alert text
Success_Message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

#- Assert that it contains "Success! Thank you!" to confirm the order was placed
assert "Success! Thank you!" in Success_Message

#- Quit the WebDriver session to close the browser.
driver.quit()
