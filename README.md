<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/sbar821/BBC-Article-Scraper">
  <!-- news icon from Icons8 -->
    <img src="assets/icons8-news-100.png" alt="News">
  </a>

<h1 align="center">BBC News  Article Scraper</h1>

  <h3 align="center">
    This webscraper takes five URLs from .txt file, scrapes them for relevant information ignoring advertisements, images, and links to other articles. It then takes the text and puts them in five separate files.
  </h3>
  <br>
  <br>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
### The file "main.py" has the code to read in links to five BBC new articles and convert them to raw text- no ads, images, or links to other articles. It utilizes beautifulsoup, a python package, and requests, a python library, to simplify the scraping process. Main calls a few different functions- one to read in links, to scrape the text, then to write to a new file. Each of these (along with main) include exception handling such as link not working or being unretrievable. 

### The file "url.txt"  contains a list of BBC World articles, each article is separated by a new line. You substitute any article for another BBC one, however anything exceeding five will not be read.

### The files such as "story1.txt" (also 2,3,4, and 5) are the articles scraped by the program. They contain a summary of each article in plain text. Upon running the program with the links, it will create them (if they are not already created, else it will overwrite them). Not necessary to run, just here to show the results of program running.

### The file "requirements.yml" contains the conda environment needed to run the code in this repository. You will need to take this file and import into your virtual environment using conda.

<!-- GETTING STARTED -->
## Getting Started

To get the web scraper up and running, these steps are operating on the assumption that you already have conda installed locally.

* Clone the repo
   ```sh
   git clone https://github.com/sbar821/BBC-Article-Scraper
   ```

* To create the conda environment, type the following:
  ```sh
  conda env create -f requirements.yml
  ```
* Find five BBC articles (or use ones already in the file) and put it into url.txt with each url terminated with a new line.


* Run main.py using the conda environment or Visual Studio Code with conda as the interpreter.

* Watch as the story1.txt and beyond are filled with the news articles selected! (Please note it only works with BBC news articles due to specific HTML tags used)

<p align="center">(<a href="#readme-top">back to top</a>)</p>
