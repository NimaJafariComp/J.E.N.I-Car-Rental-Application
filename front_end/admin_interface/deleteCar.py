from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class delete_car(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Car Deletion and Filters")

        # Main Layout
        self.main_layout = QHBoxLayout(self)

        # Filter Panel
        self.filter_panel = QVBoxLayout()
        self.filter_panel.setContentsMargins(10, 10, 10, 10)

        # Filter sections
        self.create_filter_section("Make and Model", QLineEdit())
        self.create_filter_section("Model Year (min - max)", QHBoxLayout(), ["min", "max"])
        self.create_filter_section("Paint Color", QListWidget(), is_list=True)

        # Reset Filters button
        self.reset_button = QPushButton("Reset Filters")
        self.reset_button.setFixedSize(200, 40)
        self.reset_button.setStyleSheet("background-color: #A6A6A6; color: white; border-radius: 5px;")
        self.reset_button.clicked.connect(self.reset_filters)

        # Add reset button to filter panel
        self.filter_panel.addWidget(self.reset_button, alignment=Qt.AlignCenter)

        # Car Table
        self.car_table = QTableWidget()
        self.car_table.setColumnCount(5)
        self.car_table.setHorizontalHeaderLabels(["VIN", "Model", "Make", "Year", "Color"])
        self.car_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.car_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.car_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Load Data
        self.car_data = [  # Keeping raw data to enable filtering
            {"vin": "123ABC", "model": "Model X", "make": "Tesla", "year": "2022", "color": "Red"},
            {"vin": "456DEF", "model": "Civic", "make": "Honda", "year": "2021", "color": "Blue"},
            {"vin": "789GHI", "model": "Corolla", "make": "Toyota", "year": "2020", "color": "White"},
            {"vin": "101JKL", "model": "Mustang", "make": "Ford", "year": "2023", "color": "Black"},
            {"vin": "112MNO", "model": "Model S", "make": "Tesla", "year": "2019", "color": "Silver"},
        ]
        self.load_car_data(self.car_data)

        # Delete Button
        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.setFixedSize(300, 40)
        self.delete_button.setFont(QFont("Arial", 14))
        self.delete_button.setStyleSheet("color: white; background-color: #efbe25; border-radius: 5px;")
        self.delete_button.clicked.connect(self.delete_selected)

        # Add table and delete button to main layout
        self.table_layout = QVBoxLayout()
        self.table_layout.addWidget(self.car_table)
        self.table_layout.addWidget(self.delete_button, alignment=Qt.AlignCenter)

        # Add layouts to main layout
        self.main_layout.addLayout(self.filter_panel, stretch=1)
        self.main_layout.addLayout(self.table_layout, stretch=3)

    def create_filter_section(self, label, widget, range_fields=None, is_list=False):
        """Creates a section for filters."""
        group_box = QGroupBox(label)
        group_box.setFont(QFont("Arial", 12))
        layout = QVBoxLayout()

        if is_list:
            widget.setSelectionMode(QAbstractItemView.MultiSelection)
            # Only add the specified colors
            color_options = ["Black", "Blue", "Silver", "White", "Red"]
            for color in color_options:
                item = QListWidgetItem(color)
                item.setCheckState(Qt.Unchecked)
                widget.addItem(item)
            layout.addWidget(widget)
            self.color_filter = widget  # Save for filtering logic
        elif range_fields:
            min_field = QLineEdit()
            min_field.setPlaceholderText(range_fields[0])
            max_field = QLineEdit()
            max_field.setPlaceholderText(range_fields[1])
            range_layout = QHBoxLayout()
            range_layout.addWidget(min_field)
            range_layout.addWidget(max_field)
            layout.addLayout(range_layout)
            if "Year" in label:
                self.min_year_filter = min_field
                self.max_year_filter = max_field
        else:
            layout.addWidget(widget)
            self.make_model_filter = widget  # Save for filtering logic

        group_box.setLayout(layout)
        self.filter_panel.addWidget(group_box)

    def load_car_data(self, data):
        """Loads car data into the table."""
        self.car_table.setRowCount(len(data))
        for row, car in enumerate(data):
            self.car_table.setItem(row, 0, QTableWidgetItem(car["vin"]))
            self.car_table.setItem(row, 1, QTableWidgetItem(car["model"]))
            self.car_table.setItem(row, 2, QTableWidgetItem(car["make"]))
            self.car_table.setItem(row, 3, QTableWidgetItem(car["year"]))
            self.car_table.setItem(row, 4, QTableWidgetItem(car["color"]))

    def reset_filters(self):
        """Resets all filters."""
        self.make_model_filter.clear()
        self.min_year_filter.clear()
        self.max_year_filter.clear()
        for i in range(self.color_filter.count()):
            self.color_filter.item(i).setCheckState(Qt.Unchecked)
        self.load_car_data(self.car_data)  # Reset table to show all data

    def apply_filters(self):
        """Applies filters to the car table and returns the data that meets the filters, excluding discarded data."""
        filtered_data = self.car_data[:]  # Start with all data to apply filters on
        discarded_data = []  # List to hold discarded cars

        # Filter by Make and Model
        make_model = self.make_model_filter.text()
        if make_model:
            filtered_data = [car for car in filtered_data if
                             make_model.lower() in car["make"].lower() or make_model.lower() in car["model"].lower()]
            discarded_data = [car for car in self.car_data if car not in filtered_data]

        # Filter by Year Range (minimum only)
        min_year = self.min_year_filter.text()
        if min_year.isdigit():
            min_year = int(min_year)
            # Keep cars that are equal to or greater than the minimum year and discard the rest
            cars_above_min_year = [car for car in filtered_data if int(car["year"]) >= min_year]
            discarded_data.extend([car for car in filtered_data if int(car["year"]) < min_year])
            filtered_data = cars_above_min_year

        # Filter by Paint Color
        selected_colors = [self.color_filter.item(i).text() for i in range(self.color_filter.count()) if
                           self.color_filter.item(i).checkState() == Qt.Checked]
        if selected_colors:
            # Further filter to keep only cars matching the selected colors
            cars_matching_colors = [car for car in filtered_data if car["color"] in selected_colors]
            discarded_data.extend([car for car in filtered_data if car not in cars_matching_colors])
            filtered_data = cars_matching_colors

        # Remove duplicates in discarded_data
        discarded_data = [dict(t) for t in {tuple(d.items()) for d in discarded_data}]

        return filtered_data, discarded_data  # Return both the filtered data and the discarded data

    def delete_selected(self):
        """Deletes rows matching any of the applied filters."""
        # Get the filter criteria
        make_model = self.make_model_filter.text().strip()
        min_year = self.min_year_filter.text().strip()
        max_year = self.max_year_filter.text().strip()
        selected_colors = [self.color_filter.item(i).text() for i in range(self.color_filter.count()) if
                           self.color_filter.item(i).checkState() == Qt.Checked]

        # Create a list of rows to delete based on the filters
        rows_to_delete = []
        for row in range(self.car_table.rowCount()):
            car = {
                "vin": self.car_table.item(row, 0).text(),
                "model": self.car_table.item(row, 1).text(),
                "make": self.car_table.item(row, 2).text(),
                "year": self.car_table.item(row, 3).text(),
                "color": self.car_table.item(row, 4).text(),
            }

            # Initialize flags for each filter
            matches_make_model = False
            matches_year_range = False
            matches_color = False

            # Check if the car matches the Make/Model filter
            if make_model:
                matches_make_model = make_model.lower() in car["make"].lower() or make_model.lower() in car[
                    "model"].lower()

            # Check if the car matches the Year range filter
            if min_year and min_year.isdigit():
                matches_year_range = int(car["year"]) < int(min_year)
            if max_year and max_year.isdigit():
                matches_year_range = matches_year_range and int(car["year"]) >= int(max_year)

            # Check if the car matches the Color filter
            if selected_colors:
                matches_color = car["color"] in selected_colors

            # If any of the filters match, add the row index to rows_to_delete
            if matches_make_model or matches_year_range or matches_color:
                rows_to_delete.append(row)

        # Delete matching rows from the table
        if rows_to_delete:
            for row in sorted(rows_to_delete, reverse=True):
                self.car_table.removeRow(row)

            QMessageBox.information(self, "Success", "Selected rows matching the filters have been deleted!")
        else:
            QMessageBox.information(self, "No Matches", "No rows matched the selected filters.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = delete_car()
    window.show()
    sys.exit(app.exec_())