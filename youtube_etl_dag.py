from airflow.models.dag import DAG;
from airflow.operators.python import PythonOperator;
from datetime import datetime;
from youtube_Etl_channelId import youtube_etl;
from youtube_dataclean_etl import youtube_clean;

dag=DAG(
    dag_id="youtube_dag",
    catchup=False,
    start_date=datetime(2024,3,30),
    schedule="@daily",
    
)
    
data_extraction=PythonOperator(
    task_id="data_extraction",
    python_callable=youtube_etl,
    dag=dag,
)

data_transformation=PythonOperator(
    task_id="data_transformation",
    python_callable=youtube_clean,
    dag=dag,
)

data_extraction >>  data_transformation  #this is the order