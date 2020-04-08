KUBEFLOW_HOST=${1}
NAMESPACE=${2}
PIPELINE_PATH=${3}

RUN_ID=$(python3 kfp.py $KUBEFLOW_HOST $EXPERIMENT_NAME $PIPELINE_PATH)
echo "RUN ID: ${RUN_ID}"

SUCCESS="Succeeded"
STATUS="Start"
while [ "${STATUS}" != "${SUCCESS}" ]; do
  STATUS=$(kfp run list | grep "${RUN_ID}" | awk -F "|" '{ print $4 }')
  if [ "${STATUS}" == "" ]; then
    echo "Status: Pending"
  else
    echo "Status: ${STATUS}"
  fi
  sleep 5
done

echo "${STATUS}!"
