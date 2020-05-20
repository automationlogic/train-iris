# Train Iris

## Overview

The training process fetches the Iris data from BigQuery, trains a classification model, and then uploads the model to a bucket.

Training runs as a KubeFlow pipeline on KubeFlow. The way the pipeline is built and run is described as an [Argo workflow](https://towardsdatascience.com/build-your-data-pipeline-on-kubernetes-using-kubeflow-pipelines-sdk-and-argo-eef69a80237c).

Cloud Build -> kfp script -> workflow

## Prerequisites

1. [Platform bootstrap](https://github.com/automationlogic/platform-bootstrap)
2. [Analytics infra](https://github.com/automationlogic/analytics-infra)
3. [Default Service](https://github.com/automationlogic/default-service)
4. [Ingest Iris](https://github.com/automationlogic/ingest-iris)
5. [Kubeflow tools](https://github.com/automationlogic/kubeflow-tools)

## Configuration

Cloud Build takes substitution variables as input to the `workflow.yaml.tmpl` template file. This includes `$ML_MODELS_BUCKET` and `$ANALYTICS_PROJECT`. These are passed through from the [Platform Bootstrap](https://github.com/automationlogic/platform-bootstrap) process, where they are originally configured.

## Run

The pipeline is automatically triggered when code is pushed. It can also be triggered manually via the console.
