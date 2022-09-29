"""
This module is responsible for all the operations that are going to take place
"""
from dotenv import load_dotenv
import os
import logging
from utils import get_document
from utils import get_data_url
from utils import unzip
from utils import extract_data_to_csv
import xml.etree.ElementTree as ET
logging.basicConfig(filename='test.log', level=logging.INFO)


def config_env():
    """
        This loads up all the environment variables listed in .env file
    """
    load_dotenv()
    logging.info(' .env loaded')


def main() -> None:
    if not os.path.exists('./resources'):
        os.mkdir('./resources')
    logging.info('configuring env variables')
    config_env()
    get_document(os.getenv('base_url'), 'basic.xml')
    zipfile_name, data_url = get_data_url('./resources/basic.xml')
    get_document(data_url, zipfile_name)
    success = unzip(f'./resources/{zipfile_name}', f'./resources/data')
    csv_filepath = './resources/data.csv'
    with open(csv_filepath, 'w') as f:
        f.write(f"{os.getenv('csv_header')}\n")
    if success:
        files = os.listdir('./resources/data')
        for file in files:
            extract_data_to_csv(f'./resources/data/{file}', csv_filepath)


if __name__ == '__main__':
    main()
