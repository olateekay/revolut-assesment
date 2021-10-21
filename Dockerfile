FROM python:3

WORKDIR /app
ADD revolut_api/ /app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
ENV DB_PORT=5432 
ENV APP_HOST=localhost APP_PORT=5000
CMD [ "python", "app.py" ]
