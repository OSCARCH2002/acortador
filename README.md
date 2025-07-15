# Acortador de Enlaces & Generador de Códigos QR

## Descripción General
Una solución robusta y eficiente para acortar URLs y generar códigos QR de manera instantánea. Diseñado para ofrecer una experiencia moderna, segura y escalable, ideal para entornos de producción y proyectos empresariales.

---

## Implementación en Producción

### 1. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecución del Servicio (WSGI)
Se recomienda utilizar Gunicorn para entornos productivos:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
- `-w 4`: Número de workers (ajustable según recursos disponibles)
- `-b 0.0.0.0:8000`: Escucha en todas las interfaces, puerto 8000

### 3. Integración con Proxy Inverso (Nginx)
Para máxima seguridad y rendimiento, se recomienda desplegar detrás de Nginx como proxy inverso, gestionando certificados SSL y balanceo de carga.

### 4. Recomendaciones de Seguridad
- Habilitar HTTPS en todos los entornos productivos.
- Configurar `debug=False` en `app.py`.
- Implementar una base de datos para persistencia avanzada.
- Validar y limitar el tamaño de los formularios y URLs.
- Utilizar variables de entorno para la configuración sensible.

---

## Configuración mediante Variables de Entorno
- Personaliza host, puerto y modo debug utilizando variables de entorno estándar.

---

## Tecnologías Utilizadas
- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://python-pillow.org/)

---

## Autoría
Desarrollado por Oscar. Para soporte empresarial o personalización, contactar vía email. 