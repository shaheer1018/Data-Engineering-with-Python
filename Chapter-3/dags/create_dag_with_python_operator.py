from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {'owner': 'shaheer',
                'retries': 5,
                'retry_delay': timedelta(minutes=5)
}


def greet():
    print('Hello World!')

def greet2(name, age):
    print('Hello World!, My name is {name} and my age is {age}')

def get_name():
    return "Jerry"

with DAG(dag_id = 'our_dag_with_python_operator_v03',
         default_args = default_args,
         description = 'our first dag using python operator',
         start_date = datetime(2024, 5, 25, 18),
         schedule_interval = '@hourly') as dag:
    
    task1 = PythonOperator(
            task_id = 'greet',
            python_callable = greet)

    task2 = PythonOperator(
            task_id = 'greet2',
            python_callable = greet2, 
            op_kwargs = {'name': 'Tom', 'age': 20})
    
    task3 = PythonOperator(
            task_id = 'get_name',
            python_callable = get_name
    )
task1.set_downstream(task2)
task2.set_downstream(task3)