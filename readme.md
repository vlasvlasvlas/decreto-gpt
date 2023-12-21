# Decreto Milei GPT Analyze

## Porqué?

Para entender de que va el decreto.

## Cómo?

Descargando los scripts o corriendo la notebook y pudiendo asi entender los componentes del decreto haciendole preguntas al documento pdf.

## Pasos para instalación

- Tener instalado PYthon 3.9+
- Idealmente levantar un entorno virtual (ej: python -m venv venv) y usarlo (source venv/bin/activate // o en Windows: venv\Scripts\activate)
- instalar las dependencias del requirements.txt (pip install -r requirements.txt)
- tener una key de openai (te registrás y te dan una key)
- renombar el archivo .env.dummy por .env y pegar ahí tu key de openai en el API_KEY
- se recomienda usar modelos que soporten muchos tokens (+19k para el decreto xq es largo)
- revisá y ejecutá el archivo analisis.py para poder ir generando preguntaqs al doc
- revisá y utiliza el notebook analisis_con_respuestas.py para tenerlo en formato jupyter notebook o ipython con respuesta formateada en markdown


## Quiero hacer preguntas!

Descargate el repo y usalo en tu compu! haces las preguntas que necesites.

Sino: podés subir las pregs que quieras como issue y las sumo al notebook: create un issue, poné la pregunta que quieras obtener una respuesta y las sumo al notebook: https://github.com/vlasvlasvlas/decreto-gpt/issues


## Quiero ver las respuestas que ya existen

Abrite directamente el notebook donde hay respuestas a preguntas armadas, queres que suba mas preguntas? armate un issue y las voy sumando, o forkeate esto y pone las pregs que vos quieras.

Notebook : https://github.com/vlasvlasvlas/decreto-gpt/blob/main/analisis_con_respuestas.ipynb

