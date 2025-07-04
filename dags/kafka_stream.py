from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args= {
    'owner': 'Moetez',
    'start_date': datetime(2025, 6, 24)
}

def stream_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    print(res.json())

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data()