#pip install vk_api
import vk_api,time,webbrowser

f = open('StatusList.txt','r',encoding='utf-8')
a=f.readlines()
b=range(len(a))
f.close()

if input("API ключ есть?(Y/N)")==("n"or"N"):
    print('копировать между "access_гtoken=" и "&expires_in="')
    webbrowser.open("https://oauth.vk.com/authorize?client_id=8176730&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=status&response_type=token&v=5.52")
apikey=input("введите ключ\n")
timings=int(input("введите количество секунд между статусами "))
vk_session = vk_api.VkApi(token=apikey)
vk = vk_session.get_api()#крч без этого апи не читается
print("VK Status Changer включен")
print("Закройте консоль для отключения")

while True:
    try:
        vk.status.set(text='Status changer V0.0.3 By VK: vk.com/kuuhaku.dying GH: github.com/KuuhakuDying')
        time.sleep(15)
        for i in b:
            vk.status.set(text=a[i])
            time.sleep(timings)
    except vk_api.exceptions.Captcha as captcha:
        print('captcha!')
        s_id = captcha.sid # Получение sid
        webbrowser.open(captcha.get_url())# Получить ссылку на изображение капчи
        vk.status.set(text='Captcha reset', captcha_sid=s_id, captcha_key=str(input()))