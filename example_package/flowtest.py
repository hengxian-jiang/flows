from prefect import flow, task, get_run_logger
import prefect


@task
def log_task(name):
    logger = get_run_logger()
    logger.info("Hello from %s!", name)
    logger.info("Prefect Version = %s 🚀", prefect.__version__)


@flow()
def flowtest(name: str):
    log_task(name)
