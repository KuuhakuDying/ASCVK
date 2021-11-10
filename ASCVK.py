#pip install vk_api
#получение apu ключа https://vkhost.github.io
import vk_api
import time
from webbrowser import open

vk = vk_api.VkApi(token="token place")#сюды api пихать
vk_session = vk.get_api()#крч без этого апи не читается
o_status=vk_session.status.get()#сохранение текущего статуса
print("vkStatus включен")
print("закройте консоль для отключения")

sleep_0=int(5)
sleep_1=int(5)
while True:
    try:
        vk_session.status.set(text='Open Beta 0.0.2 Status changer By vk:@kuuhaki.dying')
        time.sleep(sleep_1)
        vk_session.status.set(text='First status')
        time.sleep(sleep_0)
        vk_session.status.set(text='Second status')
        time.sleep(sleep_0)

    except vk_api.exceptions.Captcha as captcha:
        print('captcha!')
        s_id = captcha.sid # Получение sid
        open(captcha.get_url())# Получить ссылку на изображение капчи
        vk_session.status.set(text='Captcha reset', captcha_sid=s_id, captcha_key=str(input()))
vk_session.status.set(text='o_stat')
