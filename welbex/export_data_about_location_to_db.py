import os

import pandas as pd
from typing import TypeAlias, Final
import psycopg2 as psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

LocationData: TypeAlias = list[any]
FILE_PATH: Final[str] = 'uszips.csv'
FIELDS_TO_EXTRACT: Final[list[str]] = ['zip',
                                       'lat',
                                       'lng',
                                       'city',
                                       'state_name',
                                       ]


def get_data_from_csv(file_path: str, fields: list[str]) -> LocationData:
    df: pd.DataFrame = pd.read_csv(file_path)
    extracted_data: LocationData = df[fields].values.tolist()
    return extracted_data


def check_data_exists(cursor) -> bool:
    cursor.execute("SELECT COUNT(*) FROM location")
    result = cursor.fetchone()
    count = result[0] if result else 0
    return count > 0


def insert_data_into_database(data: LocationData, cursor):
    cursor.executemany(
        "INSERT INTO location (postal_code, latitude, longitude, city, state) VALUES (%s, %s, %s, %s, %s)",
        data,
    )


def main():
    with psycopg2.connect(database=DB_NAME,
                          user=DB_USER,
                          password=DB_PASSWORD,
                          host=DB_HOST,
                          port=DB_PORT,
                          ) as conn:
        with conn.cursor() as cursor:
            if not check_data_exists(cursor):
                data = get_data_from_csv(file_path=FILE_PATH, fields=FIELDS_TO_EXTRACT)
                insert_data_into_database(data, cursor)
                conn.commit()


if __name__ == '__main__':
    main()
