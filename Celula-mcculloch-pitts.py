import numpy as np

def linear_threshold_gate(dot: int, T: float) -> int:
    #####Devuelve la salida del umbral binario#####
    #####Returns the binary threshold output#####
    if dot >= T:
        return 1
    else:
        return 0
    
def funcionAND(umbral):
    for i in range(0,4):
        activation = linear_threshold_gate(dot_products[i], umbral)
        print(f'Activation: {activation}')
    print(' ')
        
def funcionOR(umbral):
    for i in range(0,4):
        activation = linear_threshold_gate(dot_products[i], umbral)
        print(f'Activation: {activation}')
    print(' ')

    
input_table = np.array([
    [0,0], # ambos (both) no
    [0,1], # uno (one) no, uno (one) yes
    [1,0], # (one) yes, (one) no
    [1,1]  # ambos (bot) yes
])
pesos = np.array([9,2])
dot_products = input_table @ pesos
umbral = 9
print(f'Dot products: {dot_products}')
funcionAND(umbral)
funcionOR(umbral)