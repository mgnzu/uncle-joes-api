from google.cloud import bigquery
from app.db.bigquery_client import client
from app.config import PROJECT_ID, DATASET_ID

def get_menu():
    query = f'''
    SELECT
        item_name,
        size,
        price
    FROM `{PROJECT_ID}.{DATASET_ID}.menu`
    ORDER BY item_name, size
    '''

    results = client.query(query)

    menu = {}

    for row in results:
        name = row.item_name

        if name not in menu:
            menu[name] = {
                "item_name": name,
                "sizes": []
            }

        menu[name]["sizes"].append({
            "size": str(row.size),
            "price": float(row.price)
        })

    return list(menu.values())
