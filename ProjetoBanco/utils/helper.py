from datetime import datetime, date


def data_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_data(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def hora_para_str(hora: datetime) -> str:
    return hora.strftime('%H:%M:%S')


def formata_moeda_real(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def formata_texto(texto: str) -> str:
    return texto.center(61, '=')
