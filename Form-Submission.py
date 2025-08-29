from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#- Launch Chrome browser using Selenium WebDriver
driver = webdriver.Chrome()

# Opens the specified practice page in the browser.
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Locates the name input field and enters "Balaji".
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Balaji")

# Locates the email input field and enters your email.
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("balajivenkatesh124@gmail.com")

# Locates the password field and enters "123456".
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")

# Locates and clicks the checkbox to agree to terms.
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

# Locates the gender dropdown and wraps it in a Select object.
Dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))

# Selects the first option in the dropdown (usually a placeholder)
Dropdown.select_by_index(0)

# Selects "Male" from the dropdown explicitly
Dropdown.select_by_visible_text("Male")

# Clicks another checkbox (possibly newsletter or agreement).
driver.find_element(By.ID, "exampleCheck1").click()

# Clicks the first radio button (e.g., "Student").
driver.find_element(By.ID,"inlineRadio1").click()

# Fills the date field using ISO format (YYYY-MM-DD).
driver.find_element(By.NAME, "bday").send_keys("2005-09-05")

#Locates and clicks the submit button to send the form.
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

# Extracts the success message shown after form submission
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

#Prints the success message to the console.
print(message)

# Closes the browser and ends the WebDriver session.
driver.quit()