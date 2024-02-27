"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pytube import YouTube
import os

class HelloWorld(toga.App):
    def startup(self):
        # Estrutura em coluna
        main_box = toga.Box(style=Pack(direction=COLUMN))
        # Texto
        name_label = toga.Label(
            "Digite o link do YouTube: ",
            style=Pack(padding=(0, 5))
        )
        # Caixa de texto
        self.name_input = toga.TextInput(style=Pack(flex=1))
        # caixa para colocar label e input
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        # Botão
        button = toga.Button(
            " Converter",
            on_press=self.convertMp4,
            # on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
       
    def convertMp4(self, e):
        url = self.name_input.value
        try:
            yt = YouTube(url)
            ytStream = yt.streams
            video = ytStream.filter(only_audio=True).first()
            download_file = video.download()
            
            base, ext = os.path.splitext(download_file)
            new_file = base + '.mp3'
            os.rename(download_file, new_file)
            
            # mensagens.value = "Sucesso na conversão!"
            print('Sucess')
            # limpar()
        except Exception as e:
            print(f"Error: {str(e)}")
            # mensagens.value =f"Error: {str(e)}"


def main():
    return HelloWorld()
