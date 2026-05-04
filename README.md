# Anonimizador Convolucional - Laboratorio de Procesamiento de Imágenes

## 📋 Descripción

Este proyecto implementa varios scripts de Python para aplicar matrices de convolución y efectos estilísticos a imágenes usando OpenCV y NumPy. Incluye filtros como Laplaciano, relieve (Emboss) y efectos personalizados tipo "Cyberpunk".

## 🎯 Características

- ✅ Aplicación de kernels de convolución (3x3)
- ✅ Detección de bordes con Canny
- ✅ Filtro Laplaciano para bordes claros
- ✅ Filtro Emboss para efecto de relieve
- ✅ Efectos "Cyberpunk" con colores neon
- ✅ Composición y fusión de capas
- ✅ Validación de entrada de archivos

## 📁 Estructura del Proyecto

```
mi_convolucion/
├── README.md                    # Este archivo
├── .gitignore                   # Configuración de Git
├── aplicar_convolucion.py       # Script principal (último)
├── convolution_v1.0.py          # Primera versión
├── convolution_v2.0.py          # Segunda versión
├── convolution_v3.0.py          # Tercera versión
├── convolution_v4.0.py          # Cuarta versión
├── input.jpeg                   # Imagen de entrada (ejemplo)
└── perfil_*.jpg                 # Imágenes procesadas
```

## 🔧 Requisitos

- Python 3.7+
- OpenCV (`cv2`)
- NumPy
- OS (librería estándar)

### Instalación de Dependencias

```bash
pip install opencv-python numpy
```

## 🚀 Uso

### Script Principal (aplicar_convolucion.py)

```bash
python aplicar_convolucion.py
```

**Pasos que ejecuta:**

1. Carga `input.jpeg` en escala de grises
2. Aplica kernel Emboss para textura
3. Detecta bordes con Canny
4. Crea efectos neon (azul cian)
5. Fusiona las capas
6. Guarda el resultado en `perfil_cyberpunk.jpg`

### Personalización

Puedes modificar el script para cambiar:

- **Ruta de entrada:** `ruta_entrada = 'tu_imagen.jpg'`
- **Ruta de salida:** `ruta_salida = 'tu_resultado.jpg'`
- **Color neon:** Cambiar `[255, 128, 0]` (BGR) a otros valores
- **Kernel:** Usar diferentes matrices de convolución

## 📊 Kernels Disponibles

### Laplaciano (Detección de Bordes)
```
[[ 0, -1,  0]
 [-1,  4, -1]
 [ 0, -1,  0]]
```

### Emboss (Relieve)
```
[[-2, -1,  0]
 [-1,  1,  1]
 [ 0,  1,  2]]
```

## 🎨 Efectos Aplicados

| Efecto | Descripción | Salida |
|--------|-------------|--------|
| Emboss | Relieve 3D | `textura_emboss` |
| Canny | Detección de bordes | `bordes` |
| Cyberpunk | Neon + Emboss + Bordes | `perfil_cyberpunk.jpg` |

## 💡 Ejemplos de Uso

### Aplicar solo Laplaciano

```python
kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
resultado = cv2.filter2D(imagen, -1, kernel)
```

### Detectar Bordes

```python
bordes = cv2.Canny(imagen, 100, 200)
```

### Fusionar Capas

```python
resultado = cv2.addWeighted(capa1, 1.0, capa2, 1.2, 0)
```

## 📝 Versiones

- **v1.0** - Convolución básica con Laplaciano
- **v2.0** - Adición de filtro Canny
- **v3.0** - Composición de capas
- **v4.0** - Efectos cyberpunk completos

## ✨ Pasos del Algoritmo

```
1. Cargar Imagen
        ↓
2. Aplicar Emboss
        ↓
3. Detectar Bordes (Canny)
        ↓
4. Oscurecer Textura
        ↓
5. Crear Efectos Neon
        ↓
6. Fusionar Capas
        ↓
7. Guardar Resultado
```

## 🐛 Solución de Problemas

| Problema | Solución |
|----------|----------|
| `ERROR: No se pudo cargar la imagen` | Verifica que `input.jpeg` exista en el directorio |
| `AttributeError: No attribute 'imread'` | Instala OpenCV: `pip install opencv-python` |
| Error de dimensiones | Asegúrate de convertir a 3 canales antes de fusionar |

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.

## 👨‍💻 Autor

Proyecto de laboratorio de procesamiento de imágenes con convolución.

---

**Última actualización:** 3 de mayo de 2026
