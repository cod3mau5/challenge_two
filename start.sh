#!/bin/bash

# Iniciar servicio webdriver-manager
webdriver-manager start &

# Activar entorno conda
source activate tiendasjumbo_spider

# Ejecutar comando de arranque
python app.py
