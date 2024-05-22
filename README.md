
# Video and explanation of the project
[Youtube](https://youtu.be/Dhenys-AI_0)


# How to run
## Install dependencies
```bash
pip install -r requirements.txt
```

## Run the project
### Run kafka docker
```
docker-compose up -d --build
```

### Run backend
```bash
export PYTHONPATH=.
python app/main.py
```

### Run consumer in multiple terminals/machines
```bash
python consumer.py
```

### Run test request
```bash
python test_request.py
```