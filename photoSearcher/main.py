from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
import requests
import wikipedia
Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):

        uq = self.manager.current_screen.ids.user_query.text

        page = wikipedia.page(uq)
        link = page.images[0]
        return link

    def download_image(self):
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        req = requests.get(self.get_image_link(), headers=headers)
        imagepath = 'images/imageFromPhotoSearcher.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
