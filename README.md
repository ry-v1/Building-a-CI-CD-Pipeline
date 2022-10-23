# Overview

This is the repository for the project "Building a CI/CD Pipeline".

In this project, we will use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install. 

Next, we will integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

Link for [Trello Board](https://trello.com/b/0YT4Wbt5/project-building-a-ci-cd-pipeline)

Link for [Project Plan](https://docs.google.com/spreadsheets/d/1JOT7QvGd7DIbNfAhEMdOAwIU5KNABhHGUieiYH2yrjw/edit#gid=1348135932)


## Instructions

* Architectural Diagram

![image](https://user-images.githubusercontent.com/72290009/184180317-6f9751fd-06b3-4cf1-af51-c6cc1ceb0012.png)

* Project running on Azure App Service


* Project cloned into Azure Cloud Shell


* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

- Adding test case for flask sklearn application

## Demo 

Link for YouTube
