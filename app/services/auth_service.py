import bcrypt
import unicodedata
from google.cloud import bigquery
from app.db.bigquery_client import client
from app.config import PROJECT_ID, DATASET_ID


def normalize_email(email: str) -> str:
    return unicodedata.normalize("NFC", email).strip().lower()


def login_user(email, password):
    email = normalize_email(email)

    query = f'''
    SELECT id, email, password
    FROM `{PROJECT_ID}.{DATASET_ID}.members`
    WHERE email = @email
    LIMIT 1
    '''

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("email", "STRING", email)
        ]
    )

    results = list(client.query(query, job_config=job_config))
    if not results:
        return None

    user = results[0]

    if not user.password:
        return None

    if bcrypt.checkpw(password.encode(), user.password.encode()):
        return {"id": user.id, "email": user.email}

    return None
