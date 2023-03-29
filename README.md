<a name="readme-top"></a>

### Built With
 * Scrapy
 * Flask
 * Selenium



<!-- GETTING STARTED -->

### Prerequisites

To run this service yout need to install docker

### Installation

_Once you installed docker follow this steps:_

1. Clone the repo
   ```sh
   git clone https://github.com/cod3mau5/challenge_two.git
   ```
2. cd into project challenge_two
   ```sh
   cd challenge_two
   ```
3. Generate Docker Image
   ```sh
   sudo docker build -t tiendasjumbo_spider:1.0 .
   ```
4. Run Docker Container
   ```sh
   sudo docker run -p 5000:5000 tiendasjumbo_spider:1.0
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Enter your Browser and type: http://127.0.0.1:5000 or see the terminal yout will see something like:
    Running on http://127.0.0.1:5000 that will be the addres you need to type on your browser

2. Now you can enter any of the url of the tiendasjumbo site menu for example: https://www.tiendasjumbo.co/herramientas-y-ferreteria/iluminacion-y-electricos/bombillos?order=OrderByBestDiscountDESC
and press "enviar" button

NOTE: some url can delay more than 10 minutes

 * IMPORTANT:
 Maybe chrome limits the timeout of a long duration http request so for this spider I recommend using firefox or another browser without this limitation


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tomas Mauricio Arana Almeida - [@codemau5](https://twitter.com/codemau5) - info@codemau5.com

Project Link: [https://github.com/cod3mau5/challenge_two](https://github.com/cod3mau5/challenge_two)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
