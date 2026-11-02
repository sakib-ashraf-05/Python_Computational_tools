from model import EmployeeModel
from view import EmployeeView
from controller import EmployeeController

if __name__ == "__main__":
    model = EmployeeModel()
    view = EmployeeView()
    controller = EmployeeController(model, view)
    controller.run()