from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.dataingestion import DataIngestion
from src.DataScience import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_file()
        


if __name__ == "__main__":

    try:
         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
         obj = DataIngestionPipeline()
         obj.initiate_data_ingestion()
         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
            logger.exception(e)
            raise e




