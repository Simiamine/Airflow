from airflow.decorators import dag, task
from datetime import datetime
import random

@dag(
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    description='A simple DAG to generate and check random numbers using TaskFlow API'
)
def random_number_checker():
    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number

    @task
    def check_even_odd(number: int):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")

    num = generate_random_number()
    check_even_odd(num)

dag = random_number_checker()
