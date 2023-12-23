from view.view import View
from presenter.presenter import Presenter
from model.model import Model

if __name__ == '__main__':
    model = Model()
    presenter = Presenter()
    view = View()

    presenter.set_model(model)
    presenter.set_view(view.main_window)

    view.main_window.set_presenter(presenter)

    view.run()
