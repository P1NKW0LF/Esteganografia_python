## Que es la esteganografía?
La **estenografía** es una técnica que se utiliza para ocultar información dentro de otro tipo de datos, como imágenes, audio o texto, de manera que la información oculta pase desapercibida para quien no conozca el método. 

### Tipos de esteganografía
- esteganografía en imágenes.
- esteganografía en video.
- esteganografía en audio.
- esteganografía en texto.
- esteganografía en redes de comunicación.

#### Técnicas de  esteganografía en imágenes
La **estenografía en imágenes** utiliza diversas técnicas para ocultar datos dentro de imágenes. Estas técnicas se basan en manipular los píxeles de la imagen de manera sutil para codificar información. Las técnicas mas usadas para esto son:
- Least Significant Bit (LSB)
- Estenografía basada en la Transformada Discreta de Coseno (DCT)
- Estenografía en el Espacio de Dominio de Color
- Estenografía por Mapas de Gradientes
- Estenografía por Inserción de Píxeles
- Estenografía en Imágenes Mediante Técnicas de Codificación
- Estenografía a Través de la Modificación de la Frecuencia de Cuantificación
En este proyecto me fui por la técnica de LSB ya que tiene un impacto mínimo en la calidad visual de la imagen pero es vulnerable a modificaciones de la imagen tal como la compresión.

### Cual es el byte menos significativo?
El **bit menos significativo** es el **bit** en la **posición más baja** dentro de un número binario. Se encuentra en el extremo derecho de la representación binaria.

#### **Posición del bit menos significativo (LSB)**:
- En un número binario, los bits se enumeran de **derecha a izquierda**.
- El bit más a la derecha es el **menos significativo**, ya que representa el valor más pequeño (la potencia de 2 más baja.
- En un número binario de **n bits**, el bit menos significativo es el bit en la posición **0**.

#### Ejemplo:
Si tienes el número binario **`10110101`** (en decimal es 181), los bits se numeran de la siguiente manera (de derecha a izquierda):
```
Posición:    7 6 5 4 3 2 1 0 
Número:      1 0 1 1 0 1 0 1
```
- El bit **en la posición 0** es el **bit menos significativo**, que en este caso es **1**.
- Los demás bits tienen valores mayores en potencias de 2, por lo que son más significativos.

### Aplicaciones de la esteganografía.
- **Seguridad y privacidad**:
    - La esteganografía es utilizada en contextos donde la seguridad de la información es crucial. Por ejemplo, para ocultar mensajes cifrados, evitando la detección por parte de terceros.
- **Protección de derechos de autor**:
    - Mediante esteganografía, los creadores de contenido pueden insertar información que permita identificar al propietario original de una obra, como una marca de agua digital en una imagen o un audio.
- **Uso ilícito**:
    - La esteganografía también se ha utilizado en actividades ilegales, como la transmisión de datos robados o información sensible en canales no detectables, evitando que los sistemas de seguridad puedan identificar y bloquear las comunicaciones.

### Limitaciones
- En muchas ocasiones, la capacidad de ocultar información está limitada por el tamaño de los datos y por la calidad de la transmisión (por ejemplo, en una imagen de baja resolución, no se pueden ocultar tantos datos).
- Además, en muchos casos, los cambios realizados pueden generar distorsiones que hacen que el archivo resultante sea fácilmente identificable.

---
## Como calcular la cantidad de datos que se pueden ocultar en la imagen?

El cálculo de la cantidad de datos que puedes ocultar en una imagen depende de varios factores, como el tipo de imagen, la técnica de esteganografía utilizada, y la resolución de la imagen. 

### 1. Cálculo de la cantidad de datos que se pueden ocultar
La capacidad de ocultación de datos en una imagen depende de la cantidad de bits que se pueden modificar sin afectar de manera perceptible a la calidad visual. 

#### a) Resolución de la imagen
La resolución de la imagen se refiere al número de píxeles en la imagen. Para calcular la cantidad de píxeles en la imagen, multiplica la **ancho** de la imagen por el **alto**. Por ejemplo, si una imagen tiene una resolución de 1920x1080 píxeles:
Cantidad de pixeles = 1920×1080 = **2,073,600 pixeles**

#### b) Número de bits por píxel

En imágenes en formato RGB, cada píxel tiene tres componentes de color: rojo (R), verde (G) y azul (B). En una imagen estándar de 8 bits por canal, cada componente de color ocupa 8 bits. Por lo tanto, un píxel en una imagen RGB ocupa:

Bits por pixel = 8 (R) + 8 (G) + 8 (B) = **24 bits**

#### c) Bits disponibles para ocultar datos

Dependiendo de la técnica de esteganografía, puedes ocultar datos modificando los bits menos significativos (LSB) de cada componente de color. En el método de LSB por ejemplo, puedes modificar solo el **bit menos significativo** de cada componente de color sin que se note una diferencia visual significativa.

Bits por pixel (con LSB) = 1 (R) + 1 (G) + 1 (B) = **3 bits**

#### d) Cantidad total de datos que se pueden ocultar

Ahora sabiendo cuántos bits se pueden modificar por píxel, puedes calcular la cantidad total de datos que se pueden ocultar en toda la imagen:

Datos ocultos (en bits) = Cantidad de pixeles × Bits por pixel

Usando una resolución de 1920x1080 píxeles:

Datos ocultos = 2,073,600 × 3 = 6,220,800 bits / 8 (byte) = 777,600 bytes = 777.6 KB

Esto significa que en una imagen de 1920x1080 píxeles, puedes ocultar hasta 777.6 KB de datos utilizando el método LSB.

### 2. **Cuándo se empieza a notar visualmente la alteración**

El umbral en el que los cambios se vuelven perceptibles depende de varios factores, como el tipo de imagen (por ejemplo, imágenes de alta resolución o de baja resolución), la técnica de esteganografía utilizada, y cuántos bits se modifican por píxel.
#### a) **Uso del LSB

- **1 bit por canal**: Cuando solo se modifica el bit menos significativo de cada componente de color (1 bit por canal), los cambios suelen ser mínimos y casi siempre indetectables, especialmente en imágenes de alta resolución.
- **Más de 1 bit por canal**: Si modificas más de 1 bit por canal (por ejemplo, 2 bits por canal), los cambios se vuelven más notables. A partir de este punto, los cambios en los colores pueden ser visibles a simple vista, especialmente en áreas de la imagen que tienen tonos homogéneos o uniformes.

#### b) **Compresión de la imagen**

- **Compresión JPEG**: Las imágenes JPEG suelen perder algunos detalles debido a la compresión, lo que puede ocultar mejor la información. Sin embargo, la compresión también puede eliminar la información oculta, especialmente si se utiliza una compresión fuerte.
- **Compresión sin pérdida** (PNG, BMP): Si la imagen no es comprimida, es más probable que los datos ocultos sean visibles si se modifica una gran cantidad de bits por píxel.

#### c) **Tamaño de los datos ocultos**

- **Gran cantidad de datos**: Si ocultas una gran cantidad de información (por ejemplo, varios megabytes), los cambios pueden volverse visibles, incluso si solo modificas el bit menos significativo. La calidad de la imagen disminuye y pueden aparecer distorsiones o artefactos visuales.

---
## Código:

Este código implementa un sistema básico de **esteganografía**, que es la técnica de ocultar información dentro de un archivo, como una imagen. En este caso, el mensaje de texto se oculta en una imagen PNG utilizando la técnica de LSB. Se emplea el formato RGB de la imagen para ocultar bits del mensaje, y luego se puede extraer el mensaje oculto de la imagen.

### Librerías utilizadas:

- **PIL (Pillow)**: Librería utilizada para abrir, manipular y guardar imágenes.
- **numpy**: Se utiliza para convertir la imagen en una matriz de valores numéricos que representan los píxeles de la imagen, facilitando el proceso de modificación y análisis.

### Funciones del código:

#### 1. `ocultar_mensaje'

Esta función se encarga de ocultar un mensaje dentro de una imagen.

##### Parámetros:

- `imagen_path`: Ruta del archivo de imagen donde se ocultará el mensaje.
- `mensaje`: El mensaje que queremos ocultar (como texto).
- `output_path`: Ruta donde se guardará la imagen con el mensaje oculto.

##### Explicación:

1. **Carga de la imagen**:
    ```python
    img = Image.open(imagen_path).convert("RGB")
    ```
	La imagen se carga utilizando la librería **PIL**, y se convierte a formato RGB (Red, Green, Blue) para trabajar con los valores de los colores de los píxeles.
    
2. **Conversión del mensaje a binario**:
    ```python
    mensaje_bin = ''.join(format(ord(c), '08b') for c in mensaje) + '11111111'
    ```
	El mensaje de texto se convierte a binario. Cada carácter del mensaje se convierte a su representación binaria utilizando `ord(c)` (que obtiene el valor Unicode del carácter) y `format(..., '08b')` para convertirlo en una cadena binaria de 8 bits. Al final del mensaje se agrega un delimitador (`'11111111'`) para marcar el final del mensaje oculto.
    
3. **Modificación de los píxeles de la imagen**:
    ```python
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  
                if index < len(mensaje_bin):
                    nuevo_valor = (img_array[i, j, k] & 254) | int(mensaje_bin[index])
                    img_array[i, j, k] = nuevo_valor 
                    index += 1
    ```
	Se recorre cada píxel de la imagen. La imagen es representada como una matriz de valores RGB. En cada componente RGB (rojo, verde, azul), se utiliza la operación `& 254` para borrar el bit menos significativo (el bit de menos peso) y luego se reemplaza por el siguiente bit del mensaje binario utilizando `| int(mensaje_bin[index])`. Esto se repite hasta que se hayan ocultado todos los bits del mensaje.
	
	La operación **`& 254`** es una **operación a nivel de bits** (bitwise), y su propósito es manipular el valor de un número binario asegurándose de que el **último bit** sea **0**, sin afectar los otros bits. En el contexto de la esteganografía, este tipo de operación es útil para manipular los **últimos bits** de los valores RGB de la imagen sin alterar los otros bits.
    
4. **Guardado de la imagen modificada**:
    ```python
    nueva_img = Image.fromarray(img_array)
    nueva_img.save(output_path)
    ```
    Después de haber ocultado el mensaje, la imagen modificada se guarda en el archivo especificado por `output_path`.

--- 
#### 2. `extraer_mensaje`

Esta función se encarga de extraer el mensaje oculto de una imagen.

##### Parámetro:

- `imagen_path`: Ruta del archivo de imagen que contiene el mensaje oculto.

##### Explicación:

1. **Carga de la imagen**:
    ```python
    img = Image.open(imagen_path)
    img_array = np.array(img)
    ```
    La imagen se carga de nuevo, y se convierte en una matriz de valores numéricos para poder acceder a los píxeles.
    
2. **Extracción de los bits del mensaje oculto**:
    ```python
    mensaje_bin = ''
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  
                mensaje_bin += str(img_array[i, j, k] & 1)
    ```
    Se recorre cada píxel de la imagen y, para cada componente RGB, se obtiene el bit menos significativo utilizando `& 1`. Estos bits se concatenan para formar la cadena binaria que representa el mensaje.
    
3. **Conversión de los bits binarios a texto**:
    ```python
    mensaje = ''
    for i in range(0, len(mensaje_bin), 8):
        byte = mensaje_bin[i:i+8]
        if byte == '11111111':  
            break
        mensaje += chr(int(byte, 2))
    ```
	Una vez que se tienen todos los bits del mensaje oculto, se agrupan de 8 en 8 para formar los bytes del mensaje original. Luego, cada byte se convierte a su correspondiente carácter utilizando `chr(int(byte, 2))`. Si se encuentra el delimitador `'11111111'` (que indica el fin del mensaje), el proceso de extracción termina.
	
	En la parte de `[i:i+8]` los ':' son un slicing lo que permite seleccionar un **subconjunto** de los elementos de una secuencia sin necesidad de recorrerla manualmente.
	En este código:
	`mensaje_bin[i:i+8]`significa que **se toma una subcadena o subsecuencia** de `mensaje_bin` desde el índice `i` hasta el índice `i+8`, sin incluir el índice `i+8`.
    
4. **Devolución del mensaje**: La función devuelve el mensaje extraído de la imagen.
	```python
	print("Mensaje extraído:", extraer_mensaje('imagen_oculta.png'))
	```

---
### Uso del código:

El código se puede utilizar de la siguiente forma:

1. **Para ocultar un mensaje en una imagen**:
    ```python
    ocultar_mensaje('./Imagen_Transportadora', 'Mensaje a ocultar', './Imagen_Con_Mensaje')
    ```
    
	Este comando tomará la imagen ubicada en `'./Imagen_Transportadora'`, ocultará el mensaje `'Mensaje a ocultar'`, y guardará la imagen modificada en `'./Imagen_Con_Mensaje'`.
    
2. **Para extraer el mensaje oculto de una imagen**:
    ```python
    print("Mensaje extraído:", extraer_mensaje('imagen_oculta.png'))
    ```
    
	Este comando extraerá el mensaje oculto en la imagen `'imagen_oculta.png'` y lo imprimirá.

