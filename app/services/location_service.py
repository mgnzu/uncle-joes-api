from google.cloud import bigquery
from app.db.bigquery_client import client
from app.config import PROJECT_ID, DATASET_ID

def get_locations():
    query = f'''
    SELECT
        id,
        city,
        state,
        phone_number,
        email,
        wifi,
        drive_thru,
        door_dash,
        open_for_business,
        address_one,
        address_two,
        zip_code,
        hours_monday_open, hours_monday_close,
        hours_tuesday_open, hours_tuesday_close,
        hours_wednesday_open, hours_wednesday_close,
        hours_thursday_open, hours_thursday_close,
        hours_friday_open, hours_friday_close,
        hours_saturday_open, hours_saturday_close,
        hours_sunday_open, hours_sunday_close
    FROM `{PROJECT_ID}.{DATASET_ID}.locations`
    ORDER BY city
    '''

    results = client.query(query)

    return [
        {
            "location_id": row.id,
            "city": row.city,
            "state": row.state,
            "phone_number": row.phone_number,
            "email": row.email,
            "wifi": row.wifi,
            "drive_thru": row.drive_thru,
            "door_dash": row.door_dash,
            "open_for_business": row.open_for_business,
            "address": row.address_one,
            "address_two": row.address_two,
            "zip_code": row.zip_code,
            "hours": {
                "monday": {"open": row.hours_monday_open, "close": row.hours_monday_close},
                "tuesday": {"open": row.hours_tuesday_open, "close": row.hours_tuesday_close},
                "wednesday": {"open": row.hours_wednesday_open, "close": row.hours_wednesday_close},
                "thursday": {"open": row.hours_thursday_open, "close": row.hours_thursday_close},
                "friday": {"open": row.hours_friday_open, "close": row.hours_friday_close},
                "saturday": {"open": row.hours_saturday_open, "close": row.hours_saturday_close},
                "sunday": {"open": row.hours_sunday_open, "close": row.hours_sunday_close},
            }
        }
        for row in results
    ]
