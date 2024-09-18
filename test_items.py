from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    browser.get(link)

    # проверяем, что страница товара на сайте содержит кнопку добавления в корзину
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
    )