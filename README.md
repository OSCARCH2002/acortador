# Acortador de Enlaces + QR

## Descripción
Acorta enlaces y genera códigos QR de forma instantánea, con un diseño profesional y moderno.

---

## Despliegue en Producción

### 1. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecuta con Gunicorn (servidor WSGI recomendado)
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
- `-w 4` = 4 workers (ajusta según tu CPU)
- `-b 0.0.0.0:8000` = escucha en todas las interfaces, puerto 8000

### 3. (Opcional) Usa Nginx como proxy inverso
- Redirige el tráfico HTTPS/HTTP a Gunicorn para mayor seguridad y rendimiento.

### 4. Seguridad y buenas prácticas
- Usa HTTPS en producción.
- Cambia `debug=True` a `debug=False` en `app.py`.
- Considera usar una base de datos para persistencia real.
- Limita el tamaño de los formularios y valida URLs.

---

## Variables de entorno
- Puedes usar variables de entorno para configurar el host, puerto, y modo debug.

---

## Créditos
- Hecho con Flask, qrcode y Pillow. 