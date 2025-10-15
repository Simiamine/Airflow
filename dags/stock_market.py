from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['stock_market']
)
def stock_market():

    @task
    def hello():
        print("Stock market DAG is working ")

    hello()

stock_market()
