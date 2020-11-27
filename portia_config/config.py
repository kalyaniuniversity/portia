_CHROME_DRIVER_DESTINATION: str = "/Volumes/Vault/Developer/webdriver/chromedriver"


def get_chrome_drive_destination() -> str:
    global _CHROME_DRIVER_DESTINATION
    return _CHROME_DRIVER_DESTINATION


def set_chrome_drive_destination(dest: str):
    global _CHROME_DRIVER_DESTINATION
    _CHROME_DRIVER_DESTINATION = dest
