import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import functionCall as sf
import pandas as pd

# Define a class variable to store the pause state
pause_flag = False

# Define a variable to keep track of the current row
current_row = 0

# Define a variable to store the path of the output CSV file
output_csv_file = 'output_data.csv'
class Mainwindow(QMainWindow):

    def __init__(self):

        super(Mainwindow, self).__init__()
        self.resize(903, 582)  # Corrected line
        loadUi("pauseButton.ui", self)
        # self.sortButton.clicked.connect(self.SortButtonClicked())

        self.loading.clicked.connect(self.load_DataFromFile)
        # Connect the combo box to a function when the selection changes
        # self.sortingMenu.currentIndexChanged.connect(self.combo_box_changed)
        # Connect the push button to a function
        self.sortButton.clicked.connect(self.sort_button_click)
        self.pause.clicked.connect(self.pause_load)
        self.startButton.clicked.connect(self.resume_load)

    def sort_button_click(self):

        selected_item = self.sortingMenu.currentText()
        print(f"Selected item: {selected_item}")
        selected_column = self.columnBox.currentText()
        print(f"Selected item: {selected_column}")
        selected_order = self.sortingType.currentText()
        print(selected_order)
        n, p, d, r, re, dp, de, po = self.getDataFromTable()
        time = 0
        result = []

        if selected_column == "Name":
            result, time = sf.SortingAlgorithmFunction_Call(n, selected_order, selected_item)
            self.populate_table(result, p, d, r, re, dp, de, po)
        elif selected_column == "Price":
            result, time = sf.SortingAlgorithmFunction_Call(p, selected_order, selected_item)
            self.populate_table(n, result, d, r, re, dp, de, po)
        elif selected_column == "Description":
            result, time = sf.SortingAlgorithmFunction_Call(d, selected_order, selected_item)
            self.populate_table(n, p, result, r, re, dp, de, po)
        elif selected_column == "Ratings":
            result, time = sf.SortingAlgorithmFunction_Call(r, selected_order, selected_item)
            self.populate_table(n, p, d, result, re, dp, de, po)
        elif selected_column == "NoOfReviews":
            result, time = sf.SortingAlgorithmFunction_Call(re, selected_order, selected_item)
            self.populate_table(n, p, d, r, result, dp, de, po)
        elif selected_column == "DiscountedPrice":
            result, time = sf.SortingAlgorithmFunction_Call(dp, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, result, de, po)
        elif selected_column == "Delivery":
            result, time = sf.SortingAlgorithmFunction_Call(de, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, result, po)
        elif selected_column == "PercentageOff":
            result, time = sf.SortingAlgorithmFunction_Call(po, selected_order, selected_item)
            self.populate_table(n, p, d, r, re, dp, de, result)

        roundedtime=round(time,4)
        self.timeLable.setText(str(roundedtime)+"seconds")
        for i in range(len(result)):
            print(result[i])
        print(time)

    def load_DataFromFile(self):
        with open("C:\\DSA\\Scraping Mid Project\\Srapping 2022-CS-63,75\\DSAMidProjectPID36\\Final.csv", 'r', encoding='iso-8859-1',
                  errors='replace') as fileInput:
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.tableWidget.setRowCount(len(self.data))
            for row in self.data:
                self.tableWidget.setItem(
                    tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.tableWidget.setItem(
                    tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.tableWidget.setItem(
                    tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.tableWidget.setItem(
                    tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.tableWidget.setItem(
                    tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.tableWidget.setItem(
                    tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.tableWidget.setItem(
                    tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.tableWidget.setItem(
                    tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))

                tableRows += 1
    # def load_DataFromFile(self):
    #     with open("D:\\Semester3\\DSALab\\DataSet\\1Million\\amazon.csv", 'r', encoding='iso-8859-1',
    #               errors='replace') as fileInput:
    #         tableRows = 0
    #         self.data = list(csv.reader(fileInput))
    #
    #         # Set the number of rows you want to read (in this case, 20)
    #         num_rows_to_read = 5
    #
    #         self.tableWidget.setRowCount(num_rows_to_read)
    #         for row in self.data[:num_rows_to_read]:
    #             self.tableWidget.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
    #             self.tableWidget.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
    #             self.tableWidget.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
    #             self.tableWidget.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
    #             self.tableWidget.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
    #             self.tableWidget.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
    #             self.tableWidget.setItem(tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
    #             self.tableWidget.setItem(tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
    #             tableRows += 1
    import csv



    def load_Data(self):
        tableRows = self.current_row
        self.tableWidget.setRowCount(len(self.data))

        with open(self.data_csv_file, 'r') as data_csv:
            data_reader = csv.reader(data_csv)
            data = list(data_reader)
            for row in data[self.current_row:]:
                if self.pause_flag:
                    # Check if the pause button was clicked
                    # If paused, break out of the loop
                    break

                self.tableWidget.setItem(
                    tableRows, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget.setItem(
                    tableRows, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(
                    tableRows, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(
                    tableRows, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tableWidget.setItem(
                    tableRows, 4, QtWidgets.QTableWidgetItem(row[4]))

                self.tableWidget.setItem(
                    tableRows, 5, QtWidgets.QTableWidgetItem(row[5]))
                self.tableWidget.setItem(
                    tableRows, 6, QtWidgets.QTableWidgetItem(row[6]))
                self.tableWidget.setItem(
                    tableRows, 7, QtWidgets.QTableWidgetItem(row[7]))

                tableRows += 1
                self.current_row += 1

            # Save the loaded data to the output CSV file
            with open(self.output_csv_file, 'w', newline='') as output_csv:
                output_writer = csv.writer(output_csv)
                output_writer.writerows(data[:self.current_row])

    # Add functions for pausing and resuming
    def pause_load(self):
        self.pause_flag = True

    def resume_load(self):
        self.pause_flag = False
        # Call load_Data again to resume loading data
        self.load_Data()

    def load_Data(self):
        tableRows = 0
        self.tableWidget.setRowCount(len(self.data))
        for row in self.data:
            self.tableWidget.setItem(
                tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.tableWidget.setItem(
                tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.tableWidget.setItem(
                tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.tableWidget.setItem(
                tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.tableWidget.setItem(
                tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            # if int(row[5].split(":")[0]) >= int(24):
            #     row[5] = row[5][0:len(row[5])-1]
            self.tableWidget.setItem(
                tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            self.tableWidget.setItem(
                tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
            self.tableWidget.setItem(
                tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
            tableRows += 1

    def SortButtonClicked(self):
        QMessageBox.information(self, "Button Clicked", "My button was clicked!")

    def populate_table(self, Name, Price, Description, Ratings, NoOfReviews, DiscountedPrice, Delivery, perOff):
        # Clear the existing items in the tableWidget (optional)
        self.tableWidget.clearContents()

        # Assuming len(Name) is the number of rows
        num_rows = len(Name)
        self.tableWidget.setRowCount(num_rows)

        for row in range(num_rows):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Name[row])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Price[row])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Description[row])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Ratings[row])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(NoOfReviews[row])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(DiscountedPrice[row])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Delivery[row])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(perOff[row])))

    def getDataFromTable(self):
        Names = []
        Price = []
        Description = []
        Rating = []
        NoOfReview = []
        DiscountedPrice = []
        Delivery = []
        perOff = []
        for row in self.data:
            Names.append(row[0])
            Price.append(row[1])
            Description.append(row[2])
            Rating.append(row[3])
            NoOfReview.append(row[4])
            DiscountedPrice.append(row[5])
            Delivery.append(row[6])
            perOff.append(row[7])
        return Names, Price, Description, Rating, NoOfReview, DiscountedPrice, Delivery, perOff

        # Now, you have separate lists for each column of data


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
