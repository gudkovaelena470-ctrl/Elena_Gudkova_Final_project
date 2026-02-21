# ЕЛЕНА ГУДКОВА 40 КОГОРТА, Автоматизация теста к API 
from sender_stand_request import post_new_order, get_order_by_track
from data import order_body


def test_create_order_and_get_by_track():
    
    create_response = post_new_order(order_body)
    assert create_response.status_code == 201, f"Create order failed: {create_response.text}"

    create_json = create_response.json()
    track = create_json.get("track")
    assert track is not None, f"No 'track' in response: {create_json}"

    get_response = get_order_by_track(track)

    assert get_response.status_code == 200, f"Get order by track failed: {get_response.text}"

    get_json = get_response.json()
    assert "order" in get_json, f"No 'order' in response: {get_json}"
