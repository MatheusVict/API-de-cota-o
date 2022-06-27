import requests

pedido = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(pedido)
#print(pedido.json())

dicionario = pedido.json()
print(f'A cotação do dolar para o real é R${dicionario["USDBRL"]["bid"]}') # Vai pegar as informações especificas do json