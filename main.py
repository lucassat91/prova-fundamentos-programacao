
total_vendas = 0
soma_bruto = 0.0
soma_descontos = 0.0
soma_liquido = 0.0

while True:
    
    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        print() 
        
        nome_produto = input("Nome do produto: ")
        
        valor_unitario = float(input("Valor unitário: "))

        quantidade = int(input("Quantidade: "))
        
        valor_bruto = valor_unitario * quantidade
        
        if valor_bruto < 100.00:
            porcentagem = 0
            
        elif valor_bruto >= 100.00 and valor_bruto <= 499.99:
            porcentagem = 5
            
        elif valor_bruto >= 500.00 and valor_bruto <= 999.99:
            porcentagem = 10
            
        elif valor_bruto >= 1000.00:
            porcentagem = 15
            
        valor_desconto = valor_bruto * (porcentagem / 100)
        
        valor_final = valor_bruto - valor_desconto
        
        print(f"\nValor bruto da venda: R$ {valor_bruto:.2f}")
        print(f"Desconto aplicado: {porcentagem}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final da venda: R$ {valor_final:.2f}")
        print("Venda registrada com sucesso!")
        
        total_vendas = total_vendas + 1
        soma_bruto = soma_bruto + valor_bruto
        soma_descontos = soma_descontos + valor_desconto
        soma_liquido = soma_liquido + valor_final

    elif opcao == '2':
        
        if total_vendas == 0:
            print("\nNenhuma venda registrada até o momento.")
        else:
            print("\n=== RESUMO PARCIAL ===")
            print(f"Total de vendas realizadas: {total_vendas}")
            print(f"Total bruto vendido: R$ {soma_bruto:.2f}")
            print(f"Total de descontos concedidos: R$ {soma_descontos:.2f}")
            print(f"Total líquido vendido: R$ {soma_liquido:.2f}")

    elif opcao == '3':
        print("\n=== RESUMO FINAL ===")
        print(f"Total de vendas realizadas: {total_vendas}")
        print(f"Total bruto vendido: R$ {soma_bruto:.2f}")
        print(f"Total de descontos concedidos: R$ {soma_descontos:.2f}")
        print(f"Total líquido vendido: R$ {soma_liquido:.2f}")
        print("\nSistema encerrado.")
        
        break

    else:
        print("\nOpção inválida. Tente novamente.")