1. Este proyecto es sobre la creación de un sistema de simulación de ferrocarriles,
el cual consiste en un programa que es operado por un funcionario de la estación. 
Este tendrá acceso a agregar, eliminar, editar y modificar el estado de los trenes, estaciones
y rutas, también tomar decisiones de manera rápida con el fin de controlar el flujo de
pasajeros en los horarios disponibles

2. Integrantes: Josefa Farías(aka jopcat1), Isidora Llanquimán(aka Hyro404), Francisca Muñoz(aka fm437352), Catalina Provoste(aka linainana), Escarlett Vargas(aka nissydva).

3. Indicadores en la interfaz:

   - Cantidad de personas activas: Muestra el número total de personas actualmente dentro de la simulación.  
   Se actualiza a medida que las personas inician o finalizan sus recorridos entre estaciones. Con el fin de poder crear trenes 
   que vayan acorde al numero de personas dentro de la simulacion.
   - Cantidad de trenes activos:  Muestra el número total de trenes actualmente en movimiento dentro de la simulación.  
   Se actualiza a medida que los trenes terminen sus recorridos o empiecen, con el fin del que el operador pueda, con ayuda del indicador
   de personas eliminar, redireccionar, o crear más trenes. -----------

De esta manera el operario conociendo estos datos, puede tomar decisiones de manera eficaz, como por ejemplo poner más trenes
si el flujo de personas es alto. 

4. Los datos se guardarán en archivos locales con extensión .json, los que se cargarán al iniciar el sistema y se actualizarán cada vez que se realicen cambios,
   como por ejemplo, al agregar, cargar o guardar trenes.

5. Para poder acceder al archivo principal:
#bash
cd INFO081-XX-PROYECTOTRENES-3/mi_proyecto #para poder acceder a la carpeta que contiene main.py
python main.py  #para correr el main.py

#bash
cd INFO081-XX-PROYECTOTRENES-3/mi_proyecto/ui #para poder llegar a ventana.py
python ventana.py                             #para correr ventana.py

Documentacion:
- Elegimos para la creacion de trenes los parametros de nombre (para poder editarlo o eliminarlo), velocidad, num. de vagones, y capacidad de estos. Para la creacion de rutas un punto de partida y llegada y la longitud de la ruta. Y para las estaciones, nombre, región, población y si va a norte o sur. 
Cada vez que se crea alguna de las entidades quedan guardadas en un archivo .json, para poder verificar los datos.
