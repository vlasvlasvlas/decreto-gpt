# DECRETO-GPT // CHAT-DNU

## Porqué?

Con el fin de comprender el Decreto de Necesidad de Urgencia (DNU) que desregula la economía, emitido el 20 de diciembre de 2023 por el presidente Javier Milei.

Permite generar una extracción a texto del pdf, y realizar preguntas específicas al DNU utilizando modelos LLM como GPT-4-Turbo (último release) de OpenAi.


## Cómo?

Descargando los scripts o corriendo la notebook y pudiendo asi entender los componentes del decreto haciendole preguntas al documento pdf.

## Pasos para instalación

- Tener instalado Python 3.9+
- Idealmente levantar un entorno virtual (ej: python -m venv venv) y usarlo (source venv/bin/activate // o en Windows: venv\Scripts\activate)
- instalar las dependencias del requirements.txt (pip install -r requirements.txt)
- tener una key de openai (te registrás y te dan una key)
- renombar el archivo .env.dummy por .env y pegar ahí tu key de openai en el API_KEY
- se recomienda usar modelos que soporten muchos tokens (+19k para el decreto xq es largo), el mejorcito que me funcionó fue GPT-4-Turbo.
- revisá y ejecutá el archivo analisis.py para poder ir generando preguntas que necesites al doc
- revisá y utiliza el notebook analisis_con_respuestas.py para tenerlo en formato jupyter notebook o ipython con respuesta formateada en markdown, o para revisar preguntas ya hechas


## Quiero hacer preguntas!

Descargate el repo y usalo en tu compu! haces las preguntas que necesites.

Sino: podés subir las pregs que quieras como issue y las sumo al notebook: create un issue, poné la pregunta que quieras obtener una respuesta y las sumo al notebook: https://github.com/vlasvlasvlas/decreto-gpt/issues


## Quiero ver las respuestas que ya existen

Abrite directamente el notebook donde hay respuestas a preguntas armadas, queres que suba mas preguntas? armate un issue y las voy sumando, o forkeate esto y pone las pregs que vos quieras.

Notebook : https://github.com/vlasvlasvlas/decreto-gpt/blob/main/analisis_con_respuestas.ipynb


## Otras fuentes de conocimiento

- se volcó a texto utf-8 el total del documento dnu y está disponible en este repo con el nombre dnu_a_texto.txt

- @agussxng (tw) armó este detalle del DNU que también esta super bueno para entender un poco más: https://docs.google.com/document/d/1vvddhIhH5MRPc2Rk1XtkBW0PV76_y5G_5UVt8v1I61A/edit

- BLapp, Asuntos Públicos y Parlamentarios, subió un pdf el cual dejo disponible en el git (Analisis_Decreto_de_Necesidad_y_Urgencia_Bases_para_la_Reconstrucción.pdf), el cual pueden acceder, tiene una especie de diff con las modificaciones de cada ley, muy bueno.

- @rama_moyano_ (tw) creó una gui para un gpt también! necesitas plus para usarlo pero acá la info: https://twitter.com/rama_moyano_/status/1737831367218716964

- se suma una versión de langchain's chat-your-data en la carpeta de langchain-chat-your-data del repo para el que le guste meter mano desde esa perspectiva.