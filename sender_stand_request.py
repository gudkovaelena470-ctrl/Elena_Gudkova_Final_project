import requests
import configuration


def post_new_order(body: dict) -> requests.Response:
    
    url = f"{configuration.BASE_URL}{configuration.CREATE_ORDER_PATH}"
    return requests.post(url, json=body)


def get_order_by_track(track: int) -> requests.Response:
    
    url = f"{configuration.BASE_URL}{configuration.GET_ORDER_BY_TRACK_PATH}"
    return requests.get(url, params={"t": track})
