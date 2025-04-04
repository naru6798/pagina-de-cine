# coder-django

Python Comisión 75140

Alumno: Mirabel, Naren Nahuel

## De qué se trata el proyecto

El proyecto es una página web de un cine. Donde hay un apartado para empleados donde pueden manipular la base de datos del candy y de las peliculas.


## Cómo ejecutarlo
- Crear el entorno virtual escribiendo en la terminal "python -m venv .venv"
- Para activar el entorno virtual escribo .\.venv\Scripts\activate
- Instalo Django escribiendo en la terminal "pip install Django"
- Instalo "pip install django-widget-tweaks"
- Corro las migraciones con "python manage.py migrate"
- Creo un superusuario con "python manage.py createsuperuser" (opcional)
- Levanto el servidor local con "python manage.py runserver"

## Caracteristicas
1. Modelos: Crean tablas que nos sirven de base de datos
Peliculas: Aquí se almacenan las peliculas de la cartelera con su titulo, descripcion y fecha de lanzamiento
CategoriaCandy: Aquí se almacenan las categorias centrales del Candy
Candy: Aquí se almacenan cada producto dandole como identidad la categoría (dentro de las existentes en nuestro modelo CategoriaCandy), el nombre del producto y el precio
2. ...

## Mejoras a futuro
1. Agregar opcion para recuperar contraseña
2. Agregar carrito de compra para candy
3. Agregar compra de entradas
4. Agregar imágenes de portada para cada película
5. Hacer un enlace para la cartelera para que no este en el index
6. Tener un inicio de sesión aparte para los clientes y que se les sea imposible registrarse e iniciar sesion en el sector de empleados
7. Agregar la cantidad de stock disponible en el candy
