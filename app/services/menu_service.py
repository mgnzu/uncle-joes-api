from google.cloud import bigquery
from app.db.bigquery_client import client
from app.config import PROJECT_ID, DATASET_ID

def get_menu():
    query = f'''
    SELECT
        name,
        size,
        price
    FROM `{PROJECT_ID}.{DATASET_ID}.menu_items`
    ORDER BY name, size
    '''

    results = client.query(query)

    menu = {}

    for row in results:
        n = row.name

        if n not in menu:
            menu[n] = {
                "item_name": n,
                "sizes": []
            }

        menu[n]["sizes"].append({
            "size": str(row.size),
            "price": float(row.price)
        })

    return list(menu.values())
