## Arquivo contendo bibliotecas e informações do Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

wait = WebDriverWait(navegador, 10)

def main():
    navegador.get("https://www.webmotors.com.br/")

    inputPesquisa = wait.until(
        EC.element_to_be_clickable(
            By.XPATH("")
        )
    )
