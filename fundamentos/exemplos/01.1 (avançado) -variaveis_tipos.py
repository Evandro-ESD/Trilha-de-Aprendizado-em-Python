# Lista de valores
dataTypes = [
    {"data_type": "Hello World"},
    {"data_type": 20},
    {"data_type": 20.5},
    {"data_type": 1j},
    {"data_type": ["apple", "banana", "cherry"]},
    {"data_type": ("apple", "banana", "cherry")},
    {"data_type": range(6)},
    {"data_type": {"name": "John", "age": 36}},
    {"data_type": {"apple", "banana", "cherry"}},
    {"data_type": frozenset({"apple", "banana", "cherry"})},
    {"data_type": True},
    {"data_type": b"Hello"},
    {"data_type": bytearray(5)},
    {"data_type": memoryview(bytes(5))},
    {"data_type": None}
]

# Função para identificar a categoria
def categoria_tipo(valor):
    if isinstance(valor, str):
        return "Tipo de texto"
    elif isinstance(valor, (int, float, complex)):
        return "Tipos numéricos"
    elif isinstance(valor, (list, tuple, range)):
        return "Tipos de sequência"
    elif isinstance(valor, dict):
        return "Tipo de mapeamento"
    elif isinstance(valor, (set, frozenset)):
        return "Tipos de conjuntos"
    elif isinstance(valor, bool):
        return "Tipo booleano"
    elif isinstance(valor, (bytes, bytearray, memoryview)):
        return "Tipos binários"
    elif valor is None:
        return "Nenhum Tipo"
    else:
        return "Desconhecido"

# Função para mostrar tipos e categorias
def mostrar_tipos(dataTypes):
    for idx, data in enumerate(dataTypes):
        valor = data['data_type']
        print(f"{idx}: {valor} -> {type(valor).__name__} -> {categoria_tipo(valor)}")

# Testando a função
mostrar_tipos(dataTypes)
