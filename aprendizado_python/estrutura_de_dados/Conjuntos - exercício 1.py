# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.
print(f"Clientes da Nubank: {nubank}\nClientes do C6: {c6}\nClientes do Inter: {inter}")

# 02) Quais são os clientes de todas as concorrentes.
print(f"Clientes de todas as concorrentes: {nubank | c6 | inter}")

# 03) Quais são os clientes da Nubank que também são clientes do C6.
print(f"Clientes da Nubank que também são clientes do C6: {nubank & c6}")

# 04) Quais são os clientes da Nubank que também são clientes do Inter.
print(f"Clientes da Nubank que também são clientes do Inter: {nubank & inter}")

# 05) Quais são os clientes do C6 que também são clientes do Inter.
print(f"Clientes do C6 que também são clientes do Inter: {c6 & inter}")

# 06) Quais são os clientes apenas da Nubank.
print(f"Clientes apenas da Nubank: {nubank - c6 - inter}")

# 07) Quais são os clientes apenas do C6.
print(f"Clientes apenas do C6: {c6 - nubank - inter}")

# 08) Quais são os clientes apenas do Inter.
print(f"Clientes apenas do Inter: {inter - nubank - c6}")

# 09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
print(f"Clientes da Nubank e C6, mas não das duas ao mesmo tempo: {(nubank | c6) - (nubank & c6)}")

# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
print(f"Clientes da Nubank e Inter, mas não das duas ao mesmo tempo: {(nubank | inter) - (nubank & inter)}")

# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
print(f"Clientes do C6 e Inter, mas não dos dois ao mesmo tempo: {(c6 | inter) - (c6 & inter)}")

# 12) Quais são os clientes das três simultaneamente.
print(f"Clientes das três simultaneamente: {nubank & c6 & inter}")
