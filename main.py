total_vendas = 0
total_bruto = 0.0
total_descontos = 0.0
total_liquido = 0.0

while True:

    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':

        print()
        nome = input("Nome do produto: ")
        valor_unitario = float(input("Valor unitário: "))
        quantidade = int(input("Quantidade: "))

        valor_bruto = valor_unitario * quantidade

        if valor_bruto < 100:
            perc_desconto = 0
        elif valor_bruto < 500:
            perc_desconto = 5
        elif valor_bruto < 1000: 
            perc_desconto = 10
        else: 
            perc_desconto = 15
