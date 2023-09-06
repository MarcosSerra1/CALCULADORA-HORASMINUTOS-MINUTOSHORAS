# Ler dados da planilha 
import openpyxl

# Abrir planilha
planilha = openpyxl.load_workbook('evento_simplificado_-_J_S_-_VT.xlsx')
# Abrir pagina da planilha
conversao_sheet = planilha['conversao']

# acessando linha de hora e minutos
for linha in conversao_sheet.iter_rows(min_row=2):
    horas = (linha[5].value)
    minutos = (linha[6].value)

print(horas, minutos)