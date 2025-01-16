def normalize_data():
    # Implement normalization with star schema here
    pass

task3 = PythonOperator(
    task_id='normalize_data',
    python_callable=normalize_data,
    dag=dag
)
