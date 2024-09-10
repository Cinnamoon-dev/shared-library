# Shared Library
Repositório com a criação de shared libraries de C++ para Python.

### Como usar
#### 01. Criar as funções
Criar um arquivo .cpp com as funções que se quer exportar da seguinte forma:

~~~c
extern "C" type funcionName(type param, ...);
~~~

#### 02. Compilar o arquivo
Roda-se o seguinte comando para compilar esse arquivo em um shared object:

~~~bash
g++ -shared -FPIC -o lib.so lib.cpp

# ou esse, caso clone esse repo
make build
~~~

#### 03. Importar o shared object no arquivo Python
Mostrarei duas formas de fazer o resto do processo:
- Usando a biblioteca ctypes
- Usando a biblioteca cffi

~~~python
import ctypes

lib = ctypes.CDLL('./lib.so')
~~~

~~~python
from cffi import ffi

ffi = FFI()

lib = ffi.dlopen('./lib.so')
~~~

#### 03.1 Definir o protótipo da função
~~~python
# Usando CFFI
ffi.cdef("""
    void showNumbers(int n1, int n2);
    void subNumbers(int n1, int n2);
""")

# Então pode-se chamar as funções
lib.showNumbers(1, 2)
lib.subNumbers(17, 4)

# ------------------------------------------------------- #

# Usando ctypes
lib.showNumbers.restype = None
lib.showNumbers.argtypes = [ctypes.c_int, ctypes.c_int]

# Então pode-se chamar as funções
lib.showNumbers(1, 3)
~~~