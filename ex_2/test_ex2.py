

from ex_2.main_ex2 import calcular_total_pedido

def test_calcular_total_pedido_somente_um_produto():
# teste com apenas um produto pedido.
    assert calcular_total_pedido([100]) == 9.0

def test_calcular_total_pedido_com_varios_produtos():
# teste com varios produtos pedidos.
    assert calcular_total_pedido([100, 101, 105, 201]) == 41.0

def test_calcular_total_pedido_produto_invalido():
# teste com um produto inválido.
    assert calcular_total_pedido([200, 300, 104]) == 19.0

def test_calcular_total_pedido_sem_produto():
# teste com lista vázia.
    assert calcular_total_pedido([]) == 0.0

def test_calcular_total_pedido_produto_repetido():
# teste com produto repetidos.
    assert calcular_total_pedido([100, 100, 105, 200, 201, 200]) == 49.0

def test_calcular_total_prdido_todos_produtos():
# teste com todos os produtos do cardápio.
    assert calcular_total_pedido([100, 101, 102, 103, 104, 105, 200, 201]) == 84.0

def test_calcular_total_pedido_produto_inexistente():
# teste com produto inexistete no cardápio.
    assert calcular_total_pedido([300]) == 0.0

 
