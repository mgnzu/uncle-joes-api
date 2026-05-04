from google.cloud import bigquery
from app.db.bigquery_client import client
from app.config import PROJECT_ID, DATASET_ID

def get_orders(member_id):
    query = f'''
    SELECT
        o.order_id,
        o.order_date,
        o.order_total,
        l.city,
        l.state,
        oi.item_name,
        oi.quantity,
        oi.price,
        oi.size
    FROM `{PROJECT_ID}.{DATASET_ID}.orders` o
    JOIN `{PROJECT_ID}.{DATASET_ID}.locations` l
      ON o.store_id = l.id
    JOIN `{PROJECT_ID}.{DATASET_ID}.order_items` oi
      ON o.order_id = oi.order_id
    WHERE o.member_id = @member_id
    ORDER BY o.order_date DESC
    '''

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("member_id", "STRING", member_id)
        ]
    )

    results = client.query(query, job_config=job_config)

    orders = {}

    for row in results:
        oid = row.order_id
        if oid not in orders:
            orders[oid] = {
                "order_id": oid,
                "order_date": row.order_date.isoformat(),
                "order_total": float(row.order_total),
                "location": {
                    "city": row.city,
                    "state": row.state
                },
                "items": []
            }

        orders[oid]["items"].append({
            "item_name": row.item_name,
            "quantity": int(row.quantity),
            "price": float(row.price),
            "size": str(row.size)
        })

    return list(orders.values())

def get_points(member_id):
    query = f'''
    SELECT SUM(FLOOR(order_total)) as points
    FROM `{PROJECT_ID}.{DATASET_ID}.orders`
    WHERE member_id = @member_id
    '''

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("member_id", "STRING", member_id)
        ]
    )

    result = list(client.query(query, job_config=job_config))
    return int(result[0].points or 0) if result else 0
