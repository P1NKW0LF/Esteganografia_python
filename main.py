# Importaciones de librerias
from PIL import Image
import numpy as np

# Funcion de esteganografia
def ocultar_mensaje(imagen_path, mensaje, output_path):
    img = Image.open(imagen_path).convert("RGB")    #Convertir a formato RGB
    img_array = np.array(img)

    # Convertir mensaje a binario y agregar delimitador
    mensaje_bin = ''.join(format(ord(c), '08b') for c in mensaje) + '11111111'

    index = 0
    for i in range(img_array.shape[0]): # Filas
        for j in range(img_array.shape[1]): # Columnas
            for k in range(3):  # Canales RGB
                if index < len(mensaje_bin):
                    nuevo_valor = (img_array[i, j, k] & 254) | int(mensaje_bin[index])  #Remplaza el valor del LSB por el siguiente del mensaje
                    img_array[i, j, k] = nuevo_valor
                    index += 1

    nueva_img = Image.fromarray(img_array)  #Convertir array en IMG
    nueva_img.save(output_path)
    print("✅ Mensaje oculto con éxito en", output_path)


# Funcion de estegoanalisis
def extraer_mensaje(imagen_path):
    img = Image.open(imagen_path)
    img_array = np.array(img)

    mensaje_bin = ''
    for i in range(img_array.shape[0]): # filas
        for j in range(img_array.shape[1]): # Columnas
            for k in range(3):  # Canales RGB
                mensaje_bin += str(img_array[i, j, k] & 1)
    # print(mensaje_bin)


    # Convertir binario a texto
    mensaje = ''
    for i in range(0, len(mensaje_bin), 8): #Recorre la lista de 8 elementos en 8
        byte = mensaje_bin[i:i+8]   #slicing
        if byte == '11111111':
            break
        mensaje += chr(int(byte, 2))    #Convertir cada Bite en su valor
    
    return mensaje

# Llamada de funciones para uso
ocultar_mensaje('./Esteganografia_python/IDK2.png', 'Esto es secreto xd', './Esteganografia_python/resultados_ocultos/IMG_oculta.png')  #Ocultar mensaje en imagen

print("Mensaje extraído:", extraer_mensaje('./Esteganografia_python/resultados_ocultos/IMG_oculta.png'))  #Para mostrar el mensaje oculto en la imagen
