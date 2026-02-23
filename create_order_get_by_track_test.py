# ЕЛЕНА ГУДКОВА 40 КОГОРТА, Автоматизация теста к API 
from sender_stand_request import post_new_order, get_order_by_track
from data import order_body


def test_get_order_by_track():
    
    create_response = post_new_order(order_body)
    track = create_response.json()["track"]
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200
