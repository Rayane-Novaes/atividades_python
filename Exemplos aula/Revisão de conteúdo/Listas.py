
lista = [1, 3, 4, 5, 6]
print(f'Lista inicialmente: {lista}')

lista.append(9)
print(f'Lista após adicionar item: {lista}')

lista.pop()
print(f'Removendo o último item: {lista}')

lista.pop(2)
print(f'Removendo item especifico: {lista}')

# O insert precisa do index da lista e o valor a ser inserido
lista.insert(0, 'Rayane')
print(f'Resultado do insert:{lista}')

# Remove um index
del lista[0]
print(f'Utilizado o del: {lista}')

lista.clear()
print(f'Limpado a lista: {lista}')

lista = [1, 3, 9]
listaB = [2, 6, 12]

# Juntado duas listas
lista.extend(listaB)
print(lista)