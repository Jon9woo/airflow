from airflow import DAG

import datetime
import pendulum

from airflow.operators.bash import BashOperator

with DAG(
    dag_id='printExample', #일반적으로 DAG이름은 파일명과 통일하는 것 권장(헷갈림 방지)
    schedule_interval='0 0 * * *', # 분, 시, 일, 월, 요일
    start_date=pendulum.datetime(2024, 7, 14, tz="Asia/Seoul"), #UTC는 세계 표준시 한국 -9시
    catchup=False, # catchup 변수는 누락된 구간을 돌림. True로 설정 시
    #dagrun_timeout=datetime.timedelta(minutes=60),
    #tags=['example', 'example2'],
    #params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1', #객체명과 task id를 동일하게 설정(헷갈림 방지)
        bash_command='python3 /Users/jongwoom1pro/Coding/개인프로젝트/printJW.py',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2', #객체명과 task id를 동일하게 설정(헷갈림 방지)
        bash_command='python3 /Users/jongwoom1pro/Coding/개인프로젝트/printMJ.py',
    )

    bash_t1 >> bash_t2 # bash_t1이 성공하면 bash_t2 실행 