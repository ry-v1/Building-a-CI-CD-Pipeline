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


## Enhancements

- Adding test case for flask sklearn application

## Demo 

Link for YouTube
