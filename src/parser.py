import os
from tabula import read_pdf
import re
# pdf_location = "../boletins/boletim_epidemiologico_assistencial_244_covid-19_08-04-2021.pdf"
# pdf_location = "boletim_epidemiologico_assistencial_240_covid-19_01-04-2021.pdf"
pdf_folder = "../boletins"
arr = os.listdir(pdf_folder)


def extract_pdf_tabela_bairros(pdf_location):
    df = read_pdf(pdf_location, pages=2, multiple_tables=True, lattice=True)
    tabela = {}
    for index in df:
        if index.columns.str.contains("Bairro").any():
            tabela = index
            break
    tabela_bairros = tabela[1:-1]
    tabela_bairros.columns = ["bairro", "sg", "srag", "obitos"]
    tabela_bairros = tabela_bairros.astype(
        {"sg": int, "srag": int, "obitos": int})
    return tabela_bairros


# for filename in arr:
#     tabela_bairros = extract_pdf_tabela_bairros(
#         pdf_folder + "/" + filename)
#     tabela_bairros.to_csv("../" +
#                           re.search(r"covid-19\_(.*).pdf$", filename).group(1)+".csv")
