import cv2
import numpy as np
import os

# Paso 1: Definir variables para las rutas de entrada y salida
ruta_entrada = 'input.jpeg'
ruta_salida = 'perfil_matrix_anonimo.jpg' # Nuevo nombre

# Paso 2: Cargar la imagen en escala de grises
imagen = cv2.imread(ruta_entrada, cv2.IMREAD_GRAYSCALE)

# Paso 3: Validar si la imagen se cargó correctamente
if imagen is None:
    print(f"ERROR: No se pudo cargar la imagen desde la ruta: {ruta_entrada}")
    exit()

print(f"✓ Imagen cargada exitosamente")

# Paso 4: Crear el efecto de relieve (emboss) sutil para textura de fondo
kernel_emboss = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
], dtype=np.float32)
textura_emboss = cv2.filter2D(imagen, -1, kernel_emboss)
# Oscurecer un poco más la textura para que no distraiga
fondo_oscuro = cv2.convertScaleAbs(textura_emboss, alpha=0.2, beta=0)
fondo_color = cv2.cvtColor(fondo_oscuro, cv2.COLOR_GRAY2BGR)

# ==============================================================================
# NUEVO - PASO 5: CONVOLUCIÓN DESTRUCTIVA ANTES DE BORDES (Anonimización)
# ==============================================================================
print("... Aplicando convolución destructiva (Posterización) para anonimizar...")

# ESTRATEGIA: Posterización (Quantization)
# Reducimos los niveles de gris para aplanar las facciones. 
# 3 o 4 niveles suelen ser ideales para perder el detalle facial.
levels = 3
imagen_destruida = np.uint8(imagen / (256 / levels)) * (256 // (levels - 1))

# Detectar bordes en la imagen abstracta/aplanada
bordes = cv2.Canny(imagen_destruida, 50, 150)

# Dilatamos (ensanchamos) los bordes significativamente para que se fundan
# y pierdan nitidez facial.
bordes_gruesos = cv2.dilate(bordes, np.ones((5,5), np.uint8), iterations=1)
# ==============================================================================

# Paso 6: Composición y Estilización "Verde Matrix" con efecto Pixeleado INTENSO
print("... Componiendo imagen final con pixelado intenso...")

# Crear una imagen vacía a color para los bordes nítidos
efectos_neon_base = np.zeros((*imagen.shape, 3), dtype=np.uint8)

# Pintar los bordes de Canny anonimizados en Verde Matrix (BGR: [0, 255, 64])
efectos_neon_base[bordes_gruesos == 255] = [0, 255, 64]

# --- MODIFICADO: Efecto Pixeleado (8-bit) INTENSIFICADO ---
# Aumentamos el factor para bloques más grandes y agresivos
factor_pixelado = 8 # Antes era 8. Prueba 20 o 32 para más abstracto.
alto, ancho = efectos_neon_base.shape[:2]

# 1. Achicar la imagen de los bordes anonimizados
neon_pequeno = cv2.resize(efectos_neon_base, (ancho // factor_pixelado, alto // factor_pixelado), interpolation=cv2.INTER_LINEAR)

# 2. Volver a agrandarla a su tamaño original usando INTER_NEAREST 
brillo_pixeleado = cv2.resize(neon_pequeno, (ancho, alto), interpolation=cv2.INTER_NEAREST)

# --- NUEVO: Mezclar líneas nítidas con el resplandor de bloques ---
# Aumentamos la opacidad del brillo para un efecto más difuso y abstracto
efecto_neon_completo = cv2.addWeighted(efectos_neon_base, 0.8, brillo_pixeleado, 2.0, 0)
# -----------------------------------------------------------

# Fusionar el fondo oscuro con el efecto de neón completo e intenso
imagen_final = cv2.addWeighted(fondo_color, 1.0, efecto_neon_completo, 1.0, 0)

# Paso 7: Guardar la imagen procesada
cv2.imwrite(ruta_salida, imagen_final)

# Paso 8: Imprimir mensaje de confirmación
print(f"\n✓ Imagen anonimizada guardada exitosamente en: {ruta_salida}")
print(f"  Ruta completa: {os.path.abspath(ruta_salida)}")
print("\nProceso completado con éxito.")