git clone https://github.com/ry-v1/Building-a-CI-CD-Pipeline
cd Building-a-CI-CD-Pipeline
git pull
make all
az webapp up -n p06-flask-sklearn --runtime PYTHON:3.7
