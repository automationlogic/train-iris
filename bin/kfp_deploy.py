import kfp
import sys
import datetime

kubeflow_host = sys.argv[1]
experiment_name = sys.argv[2]
pipeline_path = sys.argv[3]
datetime_now = "{0}".format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
job_name="{0}_training_{1}".format(experiment_name, datetime_now)

client = kfp.Client(host=kubeflow_host)
exp = client.create_experiment(name="{0}-9".format(experiment_name))
run = client.run_pipeline(experiment_id=exp.id,job_name=job_name,pipeline_package_path=pipeline_path)

print(run.id)
