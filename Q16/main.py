from model import StudentModel
from view import StudentView
from controller import StudentController

if __name__ == "__main__":
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)
    controller.run()