from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_botoes_alerts(driver):
    actions = ActionChains(driver)

    driver.get("https://demoqa.com/buttons")
    double_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
    )
    actions.double_click(double_btn).perform()
    msg_double = driver.find_element(By.ID, "doubleClickMessage").text
    assert msg_double == "You have done a double click"

    right_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_btn).perform()
    msg_right = driver.find_element(By.ID, "rightClickMessage").text
    assert msg_right == "You have done a right click"

    simple_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    simple_btn.click()
    msg_simple = driver.find_element(By.ID, "dynamicClickMessage").text
    assert msg_simple == "You have done a dynamic click"

    driver.get("https://demoqa.com/alerts")

    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "alertButton"))
    ).click()
    alert = driver.switch_to.alert
    assert alert.text == "You clicked a button"
    alert.accept()

    
    driver.find_element(By.ID, "confirmButton").click()
    confirm = driver.switch_to.alert
    assert confirm.text == "Do you confirm action?"
    confirm.dismiss()

   
    driver.find_element(By.ID, "promtButton").click()
    prompt = driver.switch_to.alert
    prompt.send_keys("Selenium Test")
    prompt.accept()
    result = driver.find_element(By.ID, "promptResult").text
    assert "Selenium Test" in result
