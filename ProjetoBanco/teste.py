from utils.helper import str_para_data, data_para_str, formata_moeda_real
from models.cliente import Cliente

data = '26/06/1993'
data = str_para_data(data)
print(data_para_str(data))

valor = 1542.25

print(formata_moeda_real(valor))

c1: Cliente = Cliente('Ivan Caséca', 'icaseca93@gmail.com', '123.456.789-01', '26/06/1993')

print(c1)

c2: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '987.587.145-21', '10/02/1951')

print(c2)
