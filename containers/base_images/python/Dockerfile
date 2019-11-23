# use image
FROM python:3.7

# copy my code to the container
ADD . /opt/herobattleground
WORKDIR /opt/herobattleground

ENV PYTHONPATH PYTHONPATH:/opt/herobattleground

# run configuration
RUN pip install -r requirements.txt
