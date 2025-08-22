from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_preencher_formulario(driver):
    driver.find_element(By.ID, "firstName").send_keys("Daniela")
    driver.find_element(By.ID, "lastName").send_keys("Foggiatto")
    driver.find_element(By.ID, "userEmail").send_keys("teste@email.com")
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='Female']"))
    )
    element.click()
    driver.find_element(By.ID, "userNumber").send_keys("48999999999")
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
    driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[text()='Music']"))
    )
    element.click()
    driver.find_element(By.ID, "currentAddress").send_keys("Florianópolis - SC")
    driver.find_element(By.ID, "submit").click()
    title = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
    assert title == "Thanks for submitting the form"

def test_email_invalido(driver):
    driver.find_element(By.ID, "firstName").send_keys("Daniela")
    driver.find_element(By.ID, "lastName").send_keys("QA")
    driver.find_element(By.ID, "userEmail").send_keys("email-invalido")
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    submit_btn.click()


    email = driver.find_element(By.ID, "userEmail")
    assert "field-error" in email.get_attribute("class")

def test_enviar_sem_preencher(driver):
    driver.find_element(By.ID, "submit").click()
    # Verifica se o campo obrigatório ficou com borda vermelha
    nome = driver.find_element(By.ID, "firstName")
    assert "field-error" in nome.get_attribute("class") or nome.get_attribute("value") == ""
