FROM python:3.7

# -----------------------------------------------------------------#
# Configuración del proyecto                                       #
# -----------------------------------------------------------------#
COPY project /opt/app
WORKDIR /opt/app

# -----------------------------------------------------------------#
# Instalación de pip y librerías requeridas                        #
# -----------------------------------------------------------------#
RUN pip install --upgrade pip
COPY pip.conf pip.conf
ENV PIP_CONFIG_FILE pip.conf
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["python", "main.py"]