import datetime


def retrieve_computer_orders():
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    return {
        "computer_orders": [
            {
            "order_id": 1,
            "created_by": 2,
            "status": "QUEUED",
            "created_at": datetime.datetime.now(),
            "equipment": []
            }
        ]
    }


def create_computer_order(request_body):
    """
    This is a stubbed method of creating a resource. It doesn't actually do anything.
    """

    return {
    "order_id": 1,
    "created_by": request_body.get("created_by", 2),
    "status": request_body.get("status", "QUEUED"),
    "created_at": request_body.get("created_at", datetime.datetime.now()),
    "equipment": request_body.get("equipment", [])
    }
