import cv2
import numpy as np
import os

# Paso 1: Definir variables para las rutas de entrada y salida
ruta_entrada = 'input.jpeg'
ruta_salida = 'perfil_matrix_pixel.jpg' # Nuevo nombre de salida

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

# Paso 6: Composición y Estilización "Verde Matrix" con efecto Pixeleado
# Oscurecer la imagen de textura original para el fondo
fondo = cv2.convertScaleAbs(textura_emboss, alpha=0.3, beta=0)

# Convertir el fondo a 3 canales (BGR)
fondo_color = cv2.cvtColor(fondo, cv2.COLOR_GRAY2BGR)

# Crear una imagen vacía a color para los bordes nítidos
efectos_neon_nitido = np.zeros((*imagen.shape, 3), dtype=np.uint8)

# Pintar los bordes de Canny en Verde Matrix (formato BGR: B=0, G=255, R=64)
efectos_neon_nitido[bordes == 255] = [0, 255, 64]

# --- NUEVO: Efecto Pixeleado (8-bit) para el resplandor ---
# 1. Definir el tamaño de los "bloques" (entre más grande el número, más grandes los píxeles)
factor_pixelado = 10 
alto, ancho = efectos_neon_nitido.shape[:2]

# 2. Achicar la imagen de los bordes dividiendo sus dimensiones
neon_pequeno = cv2.resize(efectos_neon_nitido, (ancho // factor_pixelado, alto // factor_pixelado), interpolation=cv2.INTER_LINEAR)

# 3. Volver a agrandarla a su tamaño original usando INTER_NEAREST 
# Esto es vital para mantener los bloques cuadrados sin que se difuminen
brillo_pixeleado = cv2.resize(neon_pequeno, (ancho, alto), interpolation=cv2.INTER_NEAREST)

# Mezclamos las líneas nítidas originales con el resplandor de bloques pixeleados
efecto_neon_completo = cv2.addWeighted(efectos_neon_nitido, 1.0, brillo_pixeleado, 1.5, 0)
# -----------------------------------------------------------

# Fusionar el fondo oscuro con el efecto de neón completo
imagen_final = cv2.addWeighted(fondo_color, 1.0, efecto_neon_completo, 1.0, 0)

# Paso 7: Guardar la imagen procesada
cv2.imwrite(ruta_salida, imagen_final)

# Paso 8: Imprimir mensaje de confirmación
print(f"\n✓ Imagen procesada guardada exitosamente en: {ruta_salida}")
print(f"  Ruta completa: {os.path.abspath(ruta_salida)}")
print("\nProceso completado con éxito.")