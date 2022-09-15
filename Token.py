from enum import Enum
import re
class Tokens(Enum):
    TK_MENOR= "<"
    TK_E_NUMERO="Numero"
    TK_E_OPERACION="Operacion"
    TK_MAYOR=">"
    TK_NUMERO="[0-9]*"
    TK_SLASH="/"
    TK_OP_SUMA="SUMA"
    TK_OP_RESTA="RESTA"
    TK_OP_MULTIPLICACION="MULTIPLICACIPON"
    TK_IGUAL="="
    TK_E_TIPO="Tipo"