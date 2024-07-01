import numpy as np
def delete_11(matrix):
    A=matrix
    A = A[1:]
    A = [row[1:] for row in A]
    return(A)

def delete_1n(matrix):
    A=matrix
    A = A[1:]
    A = [row[:-1] for row in A]
    return(A)

def delete_n1(matrix):
    A=matrix
    A = A[:-1]
    A = [row[1:] for row in A]
    return(A)

def delete_nn(matrix):
    A=matrix
    A = A[:-1]
    A = [row[:-1] for row in A]
    return(A)

def delete_11_nn(matrix):
    A=matrix
    A = A[:-1]
    A = A[1:]
    A = [row[:-1] for row in A]
    A = [row[1:] for row in A]
    return(A)

def det_omidfar(matrix):
  if len(matrix)==1:
      return matrix[0][0]
  if len(matrix)==2:
      return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  
  
  m11 =det_omidfar(delete_11(matrix)) 
  m1n=det_omidfar(delete_1n(matrix))
  mn1=det_omidfar(delete_n1(matrix))
  mnn=det_omidfar(delete_nn(matrix))
  m11_nn=det_omidfar(delete_11_nn(matrix))
  if m11_nn==0:
      raise ValueError("determmina is NAN")

  return ((m11*mnn - m1n*mn1)/m11_nn)
  

matrix = [[10, 1, 3,-7], [5, 4, 1,12],[0, 2, 10,1],[4,3,20,11]]
det = det_omidfar(matrix)
print(f"det: {det}")