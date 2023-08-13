#### Generador de data (Archivo data.csv)

1. Activar entorno virtual en python en la terminal(requiere tener instalada una versión de python por ej 3.10.0)
   Windows: cd env
	    .\Scripts\activate
   Linux: source env/bin/activate

   para verificar que el entorno virtual en python está activado, como prefijo en la consola debería aparecer entre parentesis
   el nombre del entorno, en este caso (env) ruta_proyecto\...

2. Una vez validado que tenemos el entorno activado ubicarse en la misma ruta del archivo requirements.txt y ejecutar 
   "pip install -r requirements.txt" esto instalará dentro del entorno virtual todas las dependencias necesarias

3. Finalmente ejecutar el archivo python que genera el archivo csv con los registros a utilizar en nuestro proyecto Jmeter
   nos ubicamos en la misma ruta donde se encuentra el archivo generador_csv.py y ejecutamos "python generador_csv.py"
   el cual pedirá por consola la cantidad de registros a generar

4. Abrir el proyecto TestPlan.jmx en la GUI de Jmeter, ir al elemento CSV Data Set Config y en el campo "Filename" seleccionar
   el archivo data.csv generado anteriormente

5. Iniciar la ejecución a través de la GUI o por consola  Por ej: "jmeter -n -t C:\Users\Hans\Desktop\TestPlan.jmx -l result.xml"