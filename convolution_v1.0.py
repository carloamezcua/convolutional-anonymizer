import cv2
import numpy as np
import os

# Paso 1: Definir variables para las rutas de entrada y salida
ruta_entrada = 'input.jpeg'
ruta_salida = 'perfil_cyberpunk.jpg'

# Paso 2: Cargar la imagen en escala de grises
imagen = cv2.imread(ruta_entrada, cv2.IMREAD_GRAYSCALE)

# Paso 3: Validar si la imagen se cargó correctamente
if imagen is None:
    print(f"ERROR: No se pudo cargar la imagen desde la ruta: {ruta_entrada}")
    exit()

print(f"✓ Imagen cargada exitosamente")

# Paso 4: Crear el efecto de relieve (emboss) para textura
kernel_emboss = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
], dtype=np.float32)
textura_emboss = cv2.filter2D(imagen, -1, kernel_emboss)

# Paso 5: Detectar bordes claros con Canny
bordes = cv2.Canny(imagen, 100, 200)

# Paso 6: Composición y Estilización "Cyberpunk"
# Oscurecer la imagen de textura original para el fondo
fondo = cv2.convertScaleAbs(textura_emboss, alpha=0.3, beta=0)

# Convertir el fondo a 3 canales (BGR)
fondo_color = cv2.cvtColor(fondo, cv2.COLOR_GRAY2BGR)

# Crear una imagen vacía a color para los efectos de luz
efectos_neon = np.zeros((*imagen.shape, 3), dtype=np.uint8)

# Pintar los bordes de Canny en azul neón (formato BGR: B=255, G=128, R=0)
efectos_neon[bordes == 255] = [255, 128, 0]

# Fusionar el fondo oscuro con los efectos de neón
imagen_final = cv2.addWeighted(fondo_color, 1.0, efectos_neon, 1.2, 0)

# Paso 7: Guardar la imagen procesada
cv2.imwrite(ruta_salida, imagen_final)

# Paso 8: Imprimir mensaje de confirmación
print(f"\n✓ Imagen procesada guardada exitosamente en: {ruta_salida}")
print(f"  Ruta completa: {os.path.abspath(ruta_salida)}")
print("\nProceso completado con éxito.")
