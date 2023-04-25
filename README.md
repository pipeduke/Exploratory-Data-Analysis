# Exploratory-Data-Analysis
The main objective of the challenge is to perform an Exploratory Data Analysis (EDA) on the data

# Jupyter Notebook
https://colab.research.google.com/drive/1a0--Aa7iNPCpifaq_Hz4-ziYYxPlbvhs?usp=sharing

# Tech Test env

```sh
git clone
cd app
python3 -m venv env_tp
source env_tp/bin/activate
pip3 install -r requirements.txt
python3 techTest.py
```

# Tech Test Docker

```sh
git clone
cd app
docker-compose build
docker-compose up -d
docker-compose exec app-csv bash
python3 techTest.py
```
