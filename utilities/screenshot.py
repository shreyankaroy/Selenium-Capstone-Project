import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        # Create screenshots folder if it doesn't exist
        os.makedirs("screenshots", exist_ok=True)

        # Create unique timestamp
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = f"{test_name}_{timestamp}.png"

        file_path = os.path.join(
            "screenshots",
            file_name
        )

        driver.save_screenshot(file_path)

        return file_path