from random import random  # Importa função para gerar números aleatórios
from kivy.app import App  # Importa a classe principal do Kivy
from kivy.uix.widget import Widget  # Importa Widget base
from kivy.uix.button import Button  # Importa botão
from kivy.graphics import Color, Ellipse, Line  # Importa elementos gráficos

class MyPaintWidget(Widget):  # Cria um widget personalizado para desenhar

    def on_touch_down(self, touch):  # Evento ao pressionar o mouse/tela
        color = (random(), 1, 1)  # Gera cor aleatória no formato HSV
        with self.canvas:  # Desenha na tela
            Color(*color, mode='hsv')  # Define cor
            d = 30.  # Diâmetro do círculo
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))  # Desenha círculo onde tocou
            touch.ud['line'] = Line(points=(touch.x, touch.y))  # Inicia linha para desenhar

    def on_touch_move(self, touch):  # Evento ao mover o mouse/tela
        touch.ud['line'].points += [touch.x, touch.y]  # Adiciona pontos à linha para desenhar o traço

class MyPaintApp(App):  # Classe principal do aplicativo

    def build(self):  # Método de construção da interface
        parent = Widget()  # Widget principal
        self.painter = MyPaintWidget()  # Instancia o widget de desenho
        clearbtn = Button(text='Clear', size_hint=(1, None), height=50)  # Cria botão de limpar
        clearbtn.bind(on_release=self.clear_canvas)  # Liga evento de clique ao método de limpar
        parent.add_widget(self.painter)  # Adiciona widget de desenho
        parent.add_widget(clearbtn)  # Adiciona botão
        return parent  # Retorna interface

    def clear_canvas(self, obj):  # Método para limpar o desenho
        self.painter.canvas.clear()  # Limpa o canvas

if __name__ == '__main__':  # Executa o app se for o arquivo principal
    MyPaintApp().run()


