
# UV performance project

  

## Introduction

This project aims to compare the performance of installing a bunch of libraries using the uv and without it. Proofing that it can helps to decrease the pipeline deployment time.

  

## Set up

For this project, the Python version used was the **3.12.2** and pip **24.0**.

#### Running without the UV environment
``` bash
python -m venv .venvNoUv
source .venvNoUv/Scripts/activate
python performance_with_no_uv.py
deactivate
```

#### Running with the UV environment
``` bash
python -m venv .venvUv
source .venvUv/Scripts/activate
pip install uv
python performance_with_uv.py
deactivate
```

## Dockerfile

Also it's available a Dockerfile which is being used to check the project deployment runtime just to have an idea about triggering a deployment pipeline.

#### Running the Dockerfile
######  Note: Before executing the following command, it's important to change the line 20 removing/adding the uv statement.
``` bash
docker build -t <build-name> .
```

## Medium

Article created to enrich with more content.

[Improve deployment pipeline using UV library](https://medium.com/@matbrizolla/improve-deployment-pipeline-using-uv-library-ffe2b4f4da68)