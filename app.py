from pandas import DataFrame

from etl.extract import TaxiExtractor
from etl.transform import TaxiTransformer
from etl.load import TaxiLoader

from utils.helpers import Helper
from utils.constants import (
    TAXI_DATA_FILENAME,
    TAXI_DATA_URL,
    TAXI_ZONE_LOOKUP_TABLE,
    TAXI_ZONE_LOOKUP_URL,
    TRANFORMED_FILE,
    VALID_DATA_PATH,
    INVALID_DATA_PATH
)

def extract() -> list[str]:
    extract_files = [
        (TAXI_DATA_URL, TAXI_DATA_FILENAME),
        (TAXI_ZONE_LOOKUP_URL, TAXI_ZONE_LOOKUP_TABLE)
    ]

    extractor = TaxiExtractor()
    downloaded_files = []

    for url, filename in extract_files:
        downloaded_files.append(
            extractor.extract(url, filename)
        )
    
    return downloaded_files

def transform(downloaded_files: list[str]) -> DataFrame:
    transformer = TaxiTransformer()
    return transformer.transform(
        filepath=downloaded_files[0],
        filepath_lookup_table=downloaded_files[1],
        output_name=TRANFORMED_FILE
    )
 
def validate(dataframe: DataFrame) -> tuple[DataFrame, DataFrame]:
    loader = TaxiLoader()
    return loader.validate_data(dataframe)
    
def load(valid_data: DataFrame, invalid_data: DataFrame):
    loader = TaxiLoader()
    load_files = {
        VALID_DATA_PATH : valid_data,
        INVALID_DATA_PATH : invalid_data
    }

    for path, dataframe in load_files.items():
        loader.load(
            dataframe=dataframe,
            output_path=path
        )
    
def main():
    extracted_files = Helper.measure(
        "Extract",
        extract()
    )
    transformed_df = Helper.measure(
        "Transform",
        lambda: transform(extracted_files)
    )
    
    valid_data, invalid_data = Helper.measure(
        "Validate",
        lambda: validate(transformed_df)
    )
    
    Helper.measure(
        "Load",
        lambda: load(valid_data, invalid_data)
    )
    
if __name__ == "__main__":
    main()