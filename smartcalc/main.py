from model.model import Model
from presenter.presenter import Presenter
from view.view import View

if __name__ == '__main__':
    model = Model()
    presenter = Presenter()
    view = View()

    presenter.set_model(model)
    presenter.set_view(view.main_window)

    view.main_window.set_presenter(presenter)

    view.run()
