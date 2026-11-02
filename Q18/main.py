from model import SalaryReportModel
from view import SalaryReportView
from controller import SalaryReportController

if __name__ == "__main__":
    model = SalaryReportModel()
    view = SalaryReportView()
    controller = SalaryReportController(model, view)
    controller.run()