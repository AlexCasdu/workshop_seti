import json

from ant_py import Route
from ant_file import Writer
from ant_mongodb import Reader

from steps.transformation import Transformation

# ------ Obtener parametros de configuración ------
with open("config/settings.json") as json_file:
    PARAMETERS = json.load(json_file)

# ------ Instanciar las clases ------
try:
    ROUTE = Route(
        name='mongodb_to_file_demo'
    )
    SOURCE_MONGODB = Reader(
        **PARAMETERS['SOURCE_MONGODB']
    )
    TARGET_FILE = Writer(
        **PARAMETERS['TARGET_FILE']
    )
    STEP_1 = (Transformation(
        name='demo_transformation'
    ))
except Exception as error_establish:
    print('Error al establecer parametros', error_establish)

# ------ Flujo de la integración ------
try:
    ROUTE.pipe_in().source(SOURCE_MONGODB).\
        step(STEP_1).\
    to(TARGET_FILE)

    ROUTE.start()

except Exception as error_mapping:
    print('Error al mapear el Route', error_mapping)