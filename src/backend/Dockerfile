FROM python:3.11.4
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app
COPY --chown=user . $HOME/app
COPY ../requirements2.txt ~/app/requirements2.txt
COPY . .
# COPY ./data/KingLear.txt ~/app/data/KingLear.txt

RUN pip install -r requirements2.txt

CMD ["chainlit", "run", "src/UI/app.py", "--port", "7860"]