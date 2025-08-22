import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")
    driver = webdriver.Edge(options=opts)
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    
    time.sleep(10)
    

