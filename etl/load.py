from abc import ABC, abstractmethod
from utils.helpers import Helper
from pathlib import Path
import pandas as pd
from pandas import DataFrame

class Load(ABC):
    @abstractmethod
    def load(self):
        pass
    
    
class TaxiLoader(Load):
    def load(self, dataframe: DataFrame, output_path: Path):
        print(f'[LOAD] Loading {len(dataframe):,} rows data ...')
        Helper.save_to_csv(dataframe, output_path)
        print(f'[LOAD] Saved to {output_path} ...')