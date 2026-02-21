# API autotests (pytest)

## Scenario
1) Create an order  
2) Save the order track number  
3) Get order data by track  
4) Check that response code is **200**

Base URL:
- https://528ba95f-1fed-4481-adad-302930679b78.serverhub.praktikum-services.ru/

## How to run
Install dependencies (at minimum `pytest` and `requests`) and run:

```bash
pytest -v
```

## Notes
Backend logs are located at:
`/var/www/backend/logs/error.log`
