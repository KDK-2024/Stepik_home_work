from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    time.sleep(15)

    # проверяем, что страница товара на сайте содержит кнопку добавления в корзину
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
    )

    assert button is not None, 'Кнопки добавления в корзину нет на странице'