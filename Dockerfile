FROM public.ecr.aws/lambda/python:3.10
WORKDIR "${LAMBDA_TASK_ROOT}"

COPY /src/app.py .  
COPY requirements.txt .
COPY .env . 

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu 
RUN pip install -r requirements.txt 

ENV XDG_CACHE_HOME = /tmp
ENV HF_HOME = /tmp
ENV TRANSFORMERS_CACHE = /tmp
EXPOSE 5000
CMD ["app.lambda_handler"]
