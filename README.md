Readme.md

[![Build and deploy Python app to Azure Web App - p06-flask-sklearn](https://github.com/ry-v1/Building-a-CI-CD-Pipeline/actions/workflows/main_p06-flask-sklearn.yml/badge.svg)](https://github.com/ry-v1/Building-a-CI-CD-Pipeline/actions/workflows/main_p06-flask-sklearn.yml)

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

Steps:

### Part I - Creating Azure web app

1. Cloing the project into Azure Cloud Shell

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197432938-a8d1b1fa-dd92-455a-938e-50d11799ec80.png">

2. Running the `make all` command from the `Makefile`

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433136-01fc781c-c89c-43a7-bc7a-f910e7c19a73.png">

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433184-a10c1049-08c0-4e15-91be-4783d602328b.png">

3. Running azure web app

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433300-c0d59f5c-a9e7-4ee8-8247-20cbd16e0d8f.png">

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433347-5758ed1a-ea83-48b3-a2bf-390797a8a4e7.png">

4. Successful prediction from deployed flask app in Azure Cloud Shell

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433512-bf933f44-2925-4e06-92e5-302969cead35.png">

5. Output of streamed log files from deployed application

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197433639-de760aaa-ce43-4496-ac8e-b86c0075163e.png">

### Part II - Azure devops

6. Create a project in Azure Devops organization

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197496309-b5d3b0a8-4663-489f-adfe-b3d6c05c13f1.png">

7. Create a service connection

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197496760-7322a701-515c-46d2-aca1-65d7d936b343.png">

8. Create an agent pool

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197497208-7ebd74ba-45b0-4775-8ea3-139ff6d63cf0.png">

9. Create a virtual machine for Azure Devops build agent

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197497681-c3181240-7108-4857-87f3-ab0b4e0ed010.png">

10. SSH into the VM

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197497965-86679b56-ad44-4e1f-8764-f85b6b265c7b.png">

11. Install docker on VM

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197498270-74601302-8bf6-4833-8923-7001ed3a1549.png">

12. Install web agent after restarting VM.

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197498500-700529eb-bf9c-4b59-bc9c-175d6dcc3abb.png">

13. Configuring the agent VM

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197499029-1ed5d94d-c5e4-4a47-8c0b-566a95d9be00.png">

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197499143-c1d2cdb9-9714-4072-affe-3a662f6763a4.png">

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197499222-0c0b8329-f267-470a-baff-795b07a76042.png">

14. Setting up Azure pipeline

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197499280-83991b35-7fec-4a3c-baab-dfaecc910b02.png">

15. Succesfully completed Azure pipeline

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/197499483-18de347b-e354-4a14-95dc-06831f786ef8.png">

15. Load testing with locust file

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/72290009/198256293-530a3106-8c09-41bc-a065-85cae8deef42.png">

## Enhancements

- Adding more test cases for flask sklearn application

## Demo 

Link for [YouTube](https://youtu.be/Ls2ujWzRRbc)
