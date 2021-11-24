from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR%27')

listaDataAbertura = []
listaFechamentoDia = []


for i in range(1, 11):

    """
    retornoDataAbertura = navegador.find_element_by_xpath(
        f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{i}]/td[1]').text"""

    retornoDataAbertura = navegador.find_element(By.XPATH,
                                                 '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                 '2]/table/tbody/tr[1]/td[1]').text

    """
    retornoFechamentoDia = navegador.find_element_by_xpath(
        f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{i}]/td[5]').text"""

    retornoFechamentoDia = navegador.find_element(By.XPATH,
                                                  '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                  '2]/table/tbody/tr[1]/td[5]').text

    listaDataAbertura.append(retornoDataAbertura)
    listaFechamentoDia.append(retornoFechamentoDia)

print(listaDataAbertura)
print(listaFechamentoDia)

with open("names.csv", "w") as arquivo_csv:
    colunas = ["Data de Abertura", "Preço de Fechamento"]
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=";", lineterminator="\n")
    escrever.writeheader()

    for i in range(0, len(listaDataAbertura)):
        escrever.writerow(
            {"Data de Abertura": f"{listaDataAbertura[i]}", "Preço de Fechamento": f"{listaFechamentoDia[i]}"})

    arquivo_csv.close()
