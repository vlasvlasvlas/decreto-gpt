# DECRETOS-GPT // CHAT-DNUS

## Porqué?

Con el fin de comprender los Decretos de Necesidad de Urgencia (DNU) y posteriores leyes por el presidente Javier Milei.

Permite generar una extracción a texto de los pdfs, y realizar preguntas específicas al DNUs y paquetes de leyes utilizando modelos LLM como GPT-4-Turbo (último release) de OpenAi.


## Update

20/12/2023
- [x] DNU-2023-70-APN-PTE : DNU - Disposiciones que desregulan la economía.

27/12/2023
- [x] MEN-2023-7-APN-PTE :  Ómnibus - Ley de Bases y Puntos de Partida para la Libertad de los Argentinos.

## Cómo?

Descargando los scripts o corriendo las notebooks y pudiendo asi entender los componentes del decreto haciendole preguntas al documento pdf.

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

- Descargate el repo y usalo en tu compu! haces las preguntas que necesites.

- Sino: podés subir las pregs que quieras como issue y las sumo al notebook: create un issue, poné la pregunta que quieras obtener una respuesta y las sumo al notebook correspondiente: https://github.com/vlasvlasvlas/decreto-gpt/issues poniendo en el subject a que documento querés realizar la pregunta, y cuál es la pregunta.


## Quiero ver las respuestas que ya existen

Abrite directamente el notebook donde hay respuestas a preguntas armadas, queres que suba mas preguntas? armate un issue y las voy sumando, o forkeate esto y pone las pregs que vos quieras.

Notebook DNU-2023-70-APN-PTE (DNU) : https://github.com/vlasvlasvlas/decreto-gpt/blob/main/notebooks/DNU-2023-70-APN-PTE_analisis_con_respuestas.ipynb

Notebook MEN-2023-7-APN-PTE (Ley ómnibus) : https://github.com/vlasvlasvlas/decreto-gpt/blob/main/notebooks/MEN-2023-7-APN-PTE_analisis_con_respuestas.ipynb

![image](https://github.com/vlasvlasvlas/decreto-gpt/assets/4071796/ddbe1b16-7ec0-444f-9044-fc9128a81e0b)


## Langchain chat-your-data versión disponible 

Se suma una versión del gran repo de chat-your-data de langchain (https://github.com/hwchase17/chat-your-data)

- lo podés usar de la carpeta de https://github.com/vlasvlasvlas/decreto-gpt/tree/main/langchain/chat-your-data del repo para el que le guste meter mano desde esa perspectiva.
- tenes que correr ESE requirement.txt (quizá en su propio venv sería mejor!)
- YA esta creada la vector-database con el contenido de cada documento! (*.pkl)
- instalate las dependencias de la carpeta (pip install -r requirements.txt)
- Tenés que correr un export OPENAI_API_KEY=tu_clave
- Si querés crear tu propio pickle file lo podés hacer. Para correr el que creé yo, (lo hice en google colab) tenes que tener un dup de archivo sino no te levanta el front gradio. es decir, correr esto:

    ```
    cd your_python_path/site-packages/faiss
    ln -s swigfaiss.py swigfaiss_avx2.py
    ```

- Levantás la aplicación con python app.py, y listop.

## Otras fuentes de conocimiento

- se volcó a texto utf-8 el total de los documentos de dnu y leyes en la carpeta /data: https://github.com/vlasvlasvlas/decreto-gpt/tree/main/data

- @agussxng (tw) armó este detalle del DNU que también esta super bueno para entender un poco más: https://docs.google.com/document/d/1vvddhIhH5MRPc2Rk1XtkBW0PV76_y5G_5UVt8v1I61A/edit

- El siguiente link lleva a un documento de diferencias antes y después del decretazo DNU super interesante (documento creado por @seppo0010 del grupo de usuaries de datos argentina): https://seppo0010.github.io/decretazo/

- BLapp, Asuntos Públicos y Parlamentarios, subió un pdf el cual dejo disponible en el git (https://github.com/vlasvlasvlas/decreto-gpt/blob/main/data/Analisis_Decreto_de_Necesidad_y_Urgencia_Bases_para_la_Reconstruccio%CC%81n.pdf), el cual pueden acceder, tiene una especie de diff con las modificaciones de cada ley, muy bueno.

- @rama_moyano_ (tw) creó una gui para un gpt también! necesitas plus para usarlo pero acá la info: https://twitter.com/rama_moyano_/status/1737831367218716964

- se comparte en formato JSON todos los articulos normalizados en formato JSON que figuran en el MEN-2023-7-APN-PTE (Ley ómnibus): https://github.com/vlasvlasvlas/decreto-gpt/blob/main/data/MEN-2023-7-APN-PTE_leyOmnibus_20231227-192229.json (documento creado por @IqJose del grupo de usuaries de datos argentina)


- análisis del megaproyecto MEN-2023-7-APN-PTE (Ley ómnibus) en Google Drive https://docs.google.com/spreadsheets/d/1u5aHpT3SYwFjUwk8gu-5OYAEPeFFPNYdSVfab9elNBI/edit#gid=0 (documento creado por @hookdump del grupo de usuaries de datos argentina)

- + info en el grupo de usuaries de datos argentina https://t.me/+p9wJldjOIhE2N2Qx