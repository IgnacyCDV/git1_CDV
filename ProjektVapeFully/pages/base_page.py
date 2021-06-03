class BasePage():
    """
    Klasa bazowa każdej strony
    """

    def __init__(self, driver):
        print("Metoda inicjalizacyjna z BasePage")
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        print("Weryfikacja z BasePage")