from view.view import CalculatorView
from presenter.presenter import CalculatorPresenter
from model.model import CalculatorModel

if __name__ == '__main__':
    model = CalculatorModel()
    presenter = CalculatorPresenter()
    view = CalculatorView()

    presenter.set_model(model)
    presenter.set_view(view.main_window)

    view.main_window.set_presenter(presenter)

    view.run()
