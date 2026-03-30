# WebSpider_selenium
Download links listed on the main page using selenium webdriver and firefox profile


## INSTALL

<code bash>
git clone git@github.com:VAzamat/WebSpider_selenium.git
cd WebSpider_selenium/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.sample .env
source .env


</code>

## Setup and start
+ Change _FirefoxProfilePath_ variable in _.env_ the firefox profile variable
+ Change _FirefoxDestDir_ variable  in the _.env_ firefox save directory 
+ Start the program _./WebSpider.py_

<code bash>
./WebSpider.py
</code>
