import kfp
import sys
import datetime

kubeflow_host = sys.argv[1]
experiment_name = sys.argv[2]
pipeline_path = sys.argv[3]
datetime_now = f"{datetime.datetime.now():%Y%m%d_%H%M%S}"
job_name=f'{experiment_name}_training_{datetime_now}'

client = kfp.Client(host=kubeflow_host)
exp = client.create_experiment(name=f'{experiment_name}-9')
run = client.run_pipeline(experiment_id=exp.id,job_name=job_name,pipeline_package_path=pipeline_path)

print(run.id)
