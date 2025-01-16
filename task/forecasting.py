def forecasting():
    # Apply your forecasting model
    pass

task4 = PythonOperator(
    task_id='forecasting',
    python_callable=forecasting,
    dag=dag
)
