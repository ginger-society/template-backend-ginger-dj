FROM python:3.12.0-bullseye
ENV PYTHONUNBUFFERED 1
ENV env dev
WORKDIR /app
ADD . /app
COPY requirements.txt /app/requirements.txt
EXPOSE 80
RUN pip install -r requirements.txt
RUN apt update
RUN pre-commit
RUN apt install git zsh curl nano wget -y
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" -y
RUN echo "zsh" >> ~/.bashrc
