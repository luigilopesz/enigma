import numpy as np
from typing import Tuple

def tableMap():
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]}{;:",.<>/?\|`~ éáíóúâêîôûãõçÉÁÍÓÚÂÊÎÔÛÃÕÇ '
  c_list = np.array(list(chars))
  msg = ''.join(c_list)
  n = len(msg)
  matrix = []
  for i in range(n): 
    l = np.array([0] * n)
    l[i]=1
    matrix.append(np.asarray(l))
  matrix = np.asarray(matrix)
  table = {}
  for c in range(n):
    table[msg[c]] = matrix[c]
  return table

def getChar(val):
  table = tableMap()
  for k, v in table.items():
    if np.array_equal(v, val):
      return k
  
  
def gerar_matrizes_de_permutacao(N : int) -> Tuple[np.ndarray, np.ndarray]:
  P, Q = np.identity(N), np.identity(N)
  P, Q = np.random.permutation(P), np.random.permutation(Q)
  return P, Q

def encriptar_enigma(msg : str, P : np.ndarray, Q : np.ndarray) -> str:
  table = tableMap()
  matrix = []
  for c in msg:
    matrix.append(table[c])
  matrix = np.asarray(matrix)
  tm = np.transpose(matrix) 
  mp = P
  for c in range(len(msg)):
    tm[:,c] = mp @ tm[:,c]
    mp = Q @ mp
  nmsg = ''
  for c in range(len(msg)):
    char = getChar(tm[:,c])
    if char is None:
      breakpoint()
    char = getChar(tm[:,c])
    nmsg += char
  return nmsg

def decriptar_enigma(msg_enc : str, P : np.ndarray, Q : np.ndarray) -> str:
  table = tableMap()
  matrix = []
  for c in msg_enc:
    matrix.append(table[c])
  matrix = np.asarray(matrix)
  tm = np.transpose(matrix) 
  imp = np.linalg.inv(P)
  imq = np.linalg.inv(Q)
  for c in range(len(msg_enc)):
    tm[:,c] = imp @ tm[:,c]
    imp = imp @ imq
  nmsg = ''
  for c in range(len(msg_enc)):
    char = getChar(tm[:,c]) 
    if char is None:
      breakpoint()
    char = getChar(tm[:,c])
    nmsg += char
  return nmsg

def main(msg):
  p, q = gerar_matrizes_de_permutacao(121)
  a = encriptar_enigma(msg, p, q)
  msgdec = decriptar_enigma(a, p, q)
  return a, msgdec

print(main('o bolo de chocolate fica pronto quatro horas da tarde'))