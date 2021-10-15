# Active Campaign integrations

Small integration script for integrations between Active campaign and other systems. 

### Local development
1. Create virtualenv ```python3 -m venv .venv```
1. Activate ```source .venv/bin/activate```
1. Install dependencies ```pip install -r requirements.txt```

### Docker
Image: docker.io/barschool/activecampaign

Deploy
```
docker build . -t barschool/activecampaign:latest
docker push barschool/activecampaign:latest
```

