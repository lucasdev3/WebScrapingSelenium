import csv

with open("names.csv", "w") as arquivo_csv:
    colunas = ["nome", "profissao"]
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=";", lineterminator="\n")
    escrever.writeheader()
    escrever.writerow({"nome": "Renato", "profissao": "programador"})
