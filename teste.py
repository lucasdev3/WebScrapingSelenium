from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR%27')

listaDataAbertura = []
listaPrecoAbertura = []
listaPrecoAlta = []
listaPrecoBaixa = []
listaFechamentoDia = []

for i in range(1, 101):
    retornoDataAbertura = navegador.find_element(By.XPATH,
                                                 '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                 f'2]/table/tbody/tr[{i}]/td[1]').text

    retornoPrecoAbertura = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                            f'2]/table/tbody/tr[{i}]/td[2]').text

    retornoPrecoAlta = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                        f'2]/table/tbody/tr[{i}]/td[3]').text

    retornoPrecoBaixa = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                         f'2]/table/tbody/tr[{i}]/td[4]').text

    retornoFechamentoDia = navegador.find_element(By.XPATH,
                                                  '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div['
                                                  f'2]/table/tbody/tr[{i}]/td[5]').text

    listaDataAbertura.append(retornoDataAbertura)
    listaPrecoAbertura.append(retornoPrecoAbertura)
    listaPrecoAlta.append(retornoPrecoAlta)
    listaPrecoBaixa.append(retornoPrecoBaixa)
    listaFechamentoDia.append(retornoFechamentoDia)


print(listaDataAbertura)
print(listaPrecoAbertura)
print(listaPrecoAlta)
print(listaPrecoBaixa)
print(listaFechamentoDia)

with open("names.csv", "w") as arquivo_csv:
    colunas = ["Data de Abertura", "preço de abertura", "preço em alta", "preço em baixa", "preço de fechamento"]
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=";", lineterminator="\n")
    escrever.writeheader()

    for i in range(0, len(listaDataAbertura)):
        escrever.writerow(
            {"Data de Abertura": f"{listaDataAbertura[i]}",
             "preço de abertura": f"{listaPrecoAbertura[i]}",
             "preço em alta": f"{listaPrecoAlta[i]}",
             "preço em baixa": f"{listaPrecoBaixa[i]}",
             "preço de fechamento": f"{listaFechamentoDia[i]}"
             })

    arquivo_csv.close()
