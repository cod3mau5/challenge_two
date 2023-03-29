FROM continuumio/anaconda3:latest

# Instalar Chrome y ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg2 unzip
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable
COPY tiendasjumbo/chromedriver_linux64/chromedriver /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

#copiar proyecto
COPY ./ ./challenge_tiendasjumbo

# Instalar Node.js desde el repositorio
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Instalar webdriver-manager y actualizar paquetes npm
RUN npm install -g npm@latest
RUN npm install -g webdriver-manager


# Crear y activar entorno conda
RUN conda create -n tiendasjumbo_spider python=3.8
RUN echo "conda activate tiendasjumbo_spider" >> ~/.bashrc

SHELL ["/bin/bash", "--login", "-c"]

#instalar nano y frameworks para conda
RUN apt-get install nano -y
RUN conda install -n tiendasjumbo_spider scrapy
RUN conda install -n tiendasjumbo_spider selenium
RUN conda install -n tiendasjumbo_spider flask

# Agregar script para ejecutar comandos
COPY start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

# Exponer puerto
EXPOSE 5000

# Iniciar comando de arranque
WORKDIR "/challenge_tiendasjumbo/tiendasjumbo"
CMD ["bash", "/usr/local/bin/start.sh"]


# docker build -t tiendasjumbo_spider_2:1.0 .
# docker run -p 5000:5000 tiendasjumbo_spider_2:1.0