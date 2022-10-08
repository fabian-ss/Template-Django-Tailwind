Aplicación Django configurada para usar TailwindCSS, CrispyFormsTailWind, Livereload y Sqlite, junto con las variables de entono, el archivo manage.py esta modificado para iniciar el servidor con la IP actual del usuario, y, en el puerto 8080.

⚠️ Esta aplicación contiene una app llamada Tailwind que sirve como ejemplo de cómo se puede integrar todo, en la ruta principal se sirve el HMTL de ejemplo 

Para que la app funcione con todo esto se deben mantener 3 servidores ejecutándose, por lo que se necesitaran 3 terminales.

1) Servidor de Django:      el clásico para poder ejecutar la aplicación.
2) Servidor de Tailwind:    para que se aplique el diseño.
3) Servidor de Live Reload: para que se vean reflejados los cambios en el HTML o archivos estáticos al guardar.

Comandos en orden:

    LiveReloadServer:
        python manage.py livereload

    TailwindCSS: ⚠️ La terminal debe estar ubicada en la carpeta de static ⚠️ Lee la documentacion primero por la instalacion requerida, comando en package.json.
        npm start

    iniciar el servidor: ⚠️ Para cambiar la dirección IP y el puerto ir al archivo manage.py ⚠️
        python manage.py runserver

⚠️ Para cargar el estilo de Tailwind se debe ejecutar el servidor, y debe mantenerse ejecutando para poder ver los cambios en el HTML, en cuanto finalice el servidor se quedará guardada la configuración hasta ese punto, si se hacen cambios con el servidor de Tailwind apagado, no se verán reflejados los cambios hasta que vuelva a estar encendido. 

⚠️ El live reload tiene algunos fallos, requiriendo guardar hasta 2 o 3 veces en algunas ocasiones, incluso hay navegadores que no lo reconocen como Brave, este apartado es opcional pero facilita la edición de los archivos estáticos, pero aun así se puede quitar fácilmente desde el archivo settings.py, en la sección de DJANGOAPPS y MIDDLEWARE

Links:

    TailwindCSS:
        https://tailwindcss.com/docs/installation 

    CrispyFormTailWind:
        https://github.com/django-crispy-forms/crispy-tailwind   

    LiveReloadServer:
        https://github.com/tjwalch/django-livereload-server         
