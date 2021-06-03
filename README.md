# Equipo 5 Actividad Integradora 3
---
## ¿Qué hace este proyecto?
Este proyecto se realizó utilizando el modelo de YOLO (You Only Look Once). La base de datos que se utilizó es shutterstock.com, la cual está enfocada a datos en forma de imagen. El programa solicitará una al usuario un término para buscar en la base de datos y posteriormente el número de fotos que se quieren obtener. Posteriormente, el programa almacenará las imágenes obtenidas en tres folders llamados train, validation y test, en donde se enviaran el 80%, 13% y 7% de la totalidad de las imágenes encontradas, respectivamente. Dentro de los tres folder, se crean 5 categorías llamadas: hot dogs, pizza, salad, spaghetti y tacos. Al buscar las imagenes, estas son distribuidas en su respectivo folder que servían para entrenar, validar y probar el modelo predictivo. Para el entrenamiento del modelo de predicción de imágenes, se utilizó la técnica de transfer learning, en donde se utiliza un modelo previamente entrenado para transferir su conocimiento a un modelo diferente pero similar. Por último se probaron distintas configuraciones, utilizando diferentes epochs y congelando distintoas capas para obtener el modelo más preciso. Al final, se obtuvo que el modelo que predice la categoría de las imágenes de mejor manera, es con una configuración de 1 capa con 20,000 parámetros y 8 epochs, obteniendo un 80% de precisión. 
## ¿Por qué es útil este proyecto?
Este proyecto ayuda a los usuarios a entrar en contacto con el mundo de la visión por computadora por medio de algoritmos que nos solicitan términos de entrada y en base a ellos nos arrojan imágenes obtenidas de una base de datos para posteriormente ser clasificadas. Esto es muy útil porque nos brinda conocimiento y herramientas que pueden ser de gran utilidad en un sinfín de aplicaciones al realizar la clasificación de imágenes por medio de algoritmos y modelos de machine learning. Por otro lado, nos ayuda a la diversificación de imágenes en distintos folders para poder obtener información de prueba e información de entrenamiento para algún modelo determinado, en caso de ser requerido.
## ¿Cómo pueden los usuarios usar este proyecto?
Es posible utilizar este proyecto para obtener imágenes de una base de datos a través del modelo programado en el archivo de la jupyter notebook creada por el equipo 5 de la clase de computer vision. Dentro de este archivo se encuentra el código utilizado para la realización de todo lo anteriormente descrito, así como comentarios importantes que pueden guiar a los usuarios en su implementación.
## ¿En dónde pueden los usuarios conseguir ayuda con respecto a nuestro proyecto?
Cualquier duda respecto al proyecto o al modelo en sí, puede ser solucionada contactando a cualquier miembro del equipo 5.
## ¿Quién mantiene y contribuye a este proyecto?
Este proyecto es mantenido por todos los contribuyentes en su desarrollo, pertenecientes al equipo 5 de computer vision, que son los siguientes:

-Francisco Ismael Sainz Williams

-Marcelo Alejandro Salazar Martínez

-Marcelo Suarez Ponce

-Arturo Vázquez Muñoz
