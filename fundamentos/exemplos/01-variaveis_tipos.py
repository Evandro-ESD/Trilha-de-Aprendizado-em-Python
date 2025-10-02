# Fonte https://www.w3schools.com/python/python_datatypes.asp

# O Python tem os seguintes tipos de dados incorporados por padrão, nestas categorias:

# Tipo de texto:	str
# Tipos numéricos:	int, float, complex
# Tipos de sequência:	list, tuple, range
# Tipo de mapeamento:	dict
# Tipos de conjuntos:	set,frozenset
# Tipo booleano:	bool
# Tipos binários:	bytes, bytearray, memoryview
# Nenhum Tipo:	NoneType

# 0: Hello World -> str -> Tipo de texto
# 1: 20 -> int -> Tipos numéricos
# 2: 20.5 -> float -> Tipos numéricos
# 3: 1j -> complex -> Tipos numéricos
# 4: ['apple', 'banana', 'cherry'] -> list -> Tipos de sequência
# 5: ('apple', 'banana', 'cherry') -> tuple -> Tipos de sequência
# 6: range(0, 6) -> range -> Tipos de sequência
# 7: {'name': 'John', 'age': 36} -> dict -> Tipo de mapeamento
# 8: {'apple', 'cherry', 'banana'} -> set -> Tipos de conjuntos
# 9: frozenset({'apple', 'cherry', 'banana'}) -> frozenset -> Tipos de conjuntos
# 10: True -> bool -> Tipos numéricos
# 11: b'Hello' -> bytes -> Tipos binários
# 12: bytearray(b'\x00\x00\x00\x00\x00') -> bytearray -> Tipos binários
# 13: <memory at 0x00000201C5C06980> -> memoryview -> Tipos binários
# 14: None -> NoneType -> Nenhum Tipo

dataTypes = [
    {"indice": "0","data_type": "Hello World"},
    {"indice": "1","data_type": 20},
    {"indice": "2","data_type": 20.5},
    {"indice": "3","data_type": 1j},
    {"indice": "4","data_type": ["apple", "banana", "cherry"]},
    {"indice": "5","data_type": ("apple", "banana", "cherry")},
    {"indice": "6","data_type": range(6)},
    {"indice": "7","data_type": {"name": "John", "age": 36}},
    {"indice": "8","data_type": {"apple", "banana", "cherry"}},
    {"indice": "9","data_type": frozenset({"apple", "banana", "cherry"})},
    {"indice": "10","data_type": True},
    {"indice": "11","data_type": b"Hello"},
    {"indice": "12","data_type": bytearray(5)},
    {"indice": "13","data_type": memoryview(bytes(5))},
    {"indice": "14","data_type": None}
]
def mostrar_tipos(dataTypes):
   for idx, data in enumerate(dataTypes):
      print(f"Os dados da posição {idx} são do tipo: {type(data['data_type'])}")

mostrar_tipos(dataTypes)
