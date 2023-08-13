import sqlite3

conn = sqlite3.connect('desafio_dio.db')

cursor = conn.cursor()

id_conta = int(input("Digite o ID da conta que deseja apagar: "))

cursor.execute("SELECT * FROM Conta WHERE id = ?", (id_conta,))
conta = cursor.fetchone()

if conta is None:
    print("Conta não encontrada.")
else:
    id_cliente = conta[1]
    
    cursor.execute("DELETE FROM Conta WHERE id = ?", (id_conta,))
    
    cursor.execute("SELECT * FROM Conta WHERE id_cliente = ?", (id_cliente,))
    outras_contas = cursor.fetchall()
    
    if len(outras_contas) == 0:
        cursor.execute("DELETE FROM Cliente WHERE id = ?", (id_cliente,))
        
    conn.commit()
    
    print("Conta e cliente associado apagados com sucesso.")

conn.close()