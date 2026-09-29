import logging
import os


def get_logger(name):

    # Create logs folder
    os.makedirs("logs", exist_ok=True)

    log_file = os.path.join("logs", "automation.log")

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler(
            log_file,
            mode="a",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger