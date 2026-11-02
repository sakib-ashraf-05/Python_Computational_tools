from model import LibraryModel
from view import LibraryView
from controller import LibraryController

if __name__ == "__main__":
    db_model = LibraryModel()
    app_view = LibraryView()
    app_controller = LibraryController(db_model, app_view)
    app_view.mainloop()