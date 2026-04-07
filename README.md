# Electric Load Forecasting

Under graduate project on short term electric load forecasting. Data was taken from [State Load Despatch Center, Delhi](www.delhisldc.org/) website and multiple time series algorithms were implemented during the course of the project.

### Models implemented:

`models` folder contains all the algorithms/models implemented during the course of the project:

* Feed forward Neural Network [FFNN.ipynb](models/FFNN.ipynb)
* Simple Moving Average [SMA.ipynb](models/SMA.ipynb)
* Weighted Moving Average [WMA.ipynb](models/WMA.ipynb)
* Simple Exponential Smoothing [SES.ipynb](models/SES.ipynb)
* Holts Winters [HW.ipynb](models/HW.ipynb)
* Autoregressive Integrated Moving Average [ARIMA.ipynb](models/ARIMA.ipynb)
* Recurrent Neural Networks [RNN.ipynb](models/RNN.ipynb)
* Long Short Term Memory cells [LSTM.ipynb](models/LSTM.ipynb)
* Gated Recurrent Unit cells [GRU.ipynb](models/GRU.ipynb)

scripts:

* `aws_arima.py` fits ARIMA model on last one month's data and forecasts load for each day.
* `aws_rnn.py` fits RNN, LSTM, GRU on last 2 month's data and forecasts load for each day.
* `aws_smoothing.py` fits SES, SMA, WMA on last one month's data and forecasts load for each day.
* `aws.py` a scheduler to run all above three scripts everyday 00:30 IST.
* `pdq_search.py` for grid search of hyperparameters of ARIMA model on last one month's data.
* `load_scrap.py` scraps day wise load data of Delhi from [SLDC](https://www.delhisldc.org/Loaddata.aspx?mode=17/01/2018) site and stores it in csv format.
* `wheather_scrap.py` scraps day wise whether data of Delhi from [wunderground](https://www.wunderground.com/history/airport/VIDP/2017/8/1/DailyHistory.html) site and stores it in csv format.

`server` folder contains django webserver code, developed to show the implemented algorithms and compare their performance. All the implemented algorithms are being used to forecast today's Delhi electricity load [here](http://forecast.energyandsystems.com) [now deprecated]. Project report can be found in [Report](Report) folder. 

## Run Locally With .venv (macOS/Linux/Windows)

### 1) Prerequisites

* Python 3.10+ (3.11 recommended)
* Git
* Optional: Redis (only needed for Celery background tasks)

### 2) Clone and enter the project

```bash
git clone https://github.com/sanchit940/forecasting.git
cd forecasting/load_forecasting
```

### 3) Create virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
```

Windows (PowerShell or CMD):

```bat
py -m venv .venv
```

### 4) Activate virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```bat
.venv\Scripts\activate.bat
```

### 5) Install dependencies

```bash
pip install --upgrade pip
pip install -r server/requirements.txt
```

### 6) Start Django server

```bash
cd server
python manage.py migrate
python manage.py runserver
```

Open: <http://127.0.0.1:8000/>

### 7) Optional: start Celery worker and beat

Make sure Redis is running, then in separate terminals:

```bash
cd forecasting/load_forecasting/server
celery -A website worker -c1 -l info
```

```bash
cd forecasting/load_forecasting/server
celery -A website beat -l info
```

### Common fixes

* If `python` is not available, use `python3` (macOS/Linux) or `py` (Windows).
* On PowerShell, if activation is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

* `mysqlclient` may fail on some machines; the default project database is SQLite in development.

![A screenshot of the website](screenshots/website.png "A screenshot of the website")


### Team Members:

* Ayush Kumar Goyal
* Boragapu Sunil Kumar
* Srimukha Paturi
* Rishabh Agrahari

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pyaf/load_forecasting&type=Date)](https://star-history.com/#pyaf/load_forecasting&Date)
