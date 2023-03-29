#!/bin/bash

# Iniciar servicio webdriver-manager
webdriver-manager start &

# Activar entorno conda
source activate store_spiders

# Ejecutar comando de arranque
python app.py
