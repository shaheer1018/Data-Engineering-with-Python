import datetime as dt
from datetime import timedelta
import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd


PATH_DATA = '/opt/airflow/data'

def CSVToJson():
    df = pd.read_csv(os.path.join(PATH_DATA, 'data.CSV'))
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON', orient = 'records')

default_args = {'owner': 'shaheer',
                'start_date': dt.datetime(2024, 5, 25),
                'retries': 1,
                'retry_delay': dt.timedelta(minutes=5)}

with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),      
         # '0 * * * *',
         ) as dag:
     
     print_starting = BashOperator(task_id='starting', bash_command='echo "I am reading the CSV now....."')
    
     CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVToJson)


# downstream
print_starting >>  CSVJson

# upstream
CSVJson << print_starting