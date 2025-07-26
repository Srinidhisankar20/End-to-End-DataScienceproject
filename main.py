from src.DataScience import logger
from src.DataScience.pipeline.Data_ingestion_Pipeline import DataIngestionPipeline
from src.DataScience.pipeline.Data_Validation_pipeline import DataValidationPipeline
from src.DataScience.config.configuration import ConfigurationManager
STAGE_NAME = "Data Ingestion stage"

try:
         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
         obj = DataIngestionPipeline()
         obj.initiate_data_ingestion()
         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
            logger.exception(e)
            raise e

STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidationPipeline()
        data_validation.intiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


