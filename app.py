from views.AuthView import AuthView
from views.BarView import BarView

class MyApp:

    def run(self):
        av = AuthView()
        av.transfer_control = self.Bar
        av.load()


    def Bar(self):
        b = BarView()
        b.load()


app = MyApp()
app.run()
