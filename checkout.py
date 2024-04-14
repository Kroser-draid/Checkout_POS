import os
from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport
import datetime
import traceback
import subprocess

class LoginDialog(QtWidgets.QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setWindowTitle("Login")
        self.resize(300, 150)

        self.uid_label = QtWidgets.QLabel("UID:")
        self.uid_display = QtWidgets.QLineEdit()
        self.login_button = QtWidgets.QPushButton("Login")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.uid_label)
        layout.addWidget(self.uid_display)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        self.waiters_uid = {"Ayoub": "123456", "Nabil": "111111"}  # Replace with your waiter names and UIDs

        self.login_button.clicked.connect(self.login)

    def login(self):
        uid = self.uid_display.text()
        for waiter, waiter_uid in self.waiters_uid.items():
            if uid == waiter_uid:
                self.waiter_name = waiter  # Set the waiter_name attribute
                self.accept()
                return

        QtWidgets.QMessageBox.warning(self, "Invalid UID", "The UID is not recognized.")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1236, 657)

        # Add a rectangular widget
        self.rectangular_widget = QtWidgets.QWidget(Dialog)
        self.rectangular_widget.setObjectName("rectangular_widget")
        self.rectangular_widget.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")  # Set background color and border
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rectangular_widget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)  # Add margins
        self.verticalLayout.setObjectName("verticalLayout")

        # Create a button for "La Recette"
        self.receipt_button = QtWidgets.QPushButton("CAFE ROMA", self.rectangular_widget)
        self.receipt_button.setObjectName("receipt_button")
        self.receipt_button.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")  # Set font size, weight, and color
        self.receipt_button.clicked.connect(self.show_total)  # Connect button click to show_total method
        self.verticalLayout.addWidget(self.receipt_button)

        self.date_time_label = QtWidgets.QLabel(self.rectangular_widget)
        self.date_time_label.setObjectName("date_time_label")
        self.date_time_label.setStyleSheet("font-size: 16px; color: #555;")  # Set font size and color
        self.verticalLayout.addWidget(self.date_time_label)

        self.waiter_label = QtWidgets.QLabel(self.rectangular_widget)
        self.waiter_label.setObjectName("waiter_label")
        self.waiter_label.setStyleSheet("font-size: 16px; color: #555;")  # Set font size and color
        self.verticalLayout.addWidget(self.waiter_label)

        self.receipt_count_label = QtWidgets.QLabel(self.rectangular_widget)
        self.receipt_count_label.setObjectName("receipt_count_label")
        self.receipt_count_label.setStyleSheet("font-size: 16px; color: #555;")  # Set font size and color
        self.verticalLayout.addWidget(self.receipt_count_label)

        # Add the rectangular widget to the layout
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1540, 210))  # Adjusted size
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.rectangular_widget)


        # List widget and command link button
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(1240, 240, 256, 611))  # Adjusted position
        self.listWidget.setObjectName("listWidget")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(1270, 750, 186, 71))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setStyleSheet("color: #fff; background-color: #007bff; border: none;")  # Set text color and background color
        self.commandLinkButton.clicked.connect(self.generate_receipt_text)

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 826, 416))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")

        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.Tea = QtWidgets.QLabel(self.layoutWidget)
        self.Tea.setMinimumSize(QtCore.QSize(171, 181))
        self.Tea.setText("")
        self.Tea.setPixmap(QtGui.QPixmap("atai.png"))
        self.Tea.setScaledContents(True)
        self.Tea.setObjectName("Tea")
        self.gridLayout.addWidget(self.Tea, 0, 0, 1, 1)

        self.caffe_creme = QtWidgets.QLabel(self.layoutWidget)
        self.caffe_creme.setMinimumSize(QtCore.QSize(171, 181))
        self.caffe_creme.setText("")
        self.caffe_creme.setPixmap(QtGui.QPixmap("cafe_creme.png"))
        self.caffe_creme.setScaledContents(True)
        self.caffe_creme.setObjectName("caffe_creme")
        self.gridLayout.addWidget(self.caffe_creme, 0, 1, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.chocolat_chaud = QtWidgets.QLabel(self.layoutWidget)
        self.chocolat_chaud.setMinimumSize(QtCore.QSize(171, 181))
        self.chocolat_chaud.setText("")
        self.chocolat_chaud.setPixmap(QtGui.QPixmap("chocolat.png"))
        self.chocolat_chaud.setScaledContents(True)
        self.chocolat_chaud.setObjectName("chocolat_chaud")
        self.gridLayout_4.addWidget(self.chocolat_chaud, 0, 0, 1, 1)

        self.noire = QtWidgets.QLabel(self.layoutWidget)
        self.noire.setMinimumSize(QtCore.QSize(171, 181))
        self.noire.setText("")
        self.noire.setPixmap(QtGui.QPixmap("coffee.png"))
        self.noire.setScaledContents(True)
        self.noire.setObjectName("noire")
        self.gridLayout_4.addWidget(self.noire, 0, 1, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.ftour = QtWidgets.QLabel(self.layoutWidget)
        self.ftour.setMinimumSize(QtCore.QSize(171, 181))
        self.ftour.setText("")
        self.ftour.setPixmap(QtGui.QPixmap("ftor.png"))
        self.ftour.setScaledContents(True)
        self.ftour.setObjectName("ftour")
        self.gridLayout_7.addWidget(self.ftour, 0, 0, 1, 1)

        self.Soda = QtWidgets.QLabel(self.layoutWidget)
        self.Soda.setMinimumSize(QtCore.QSize(171, 181))
        self.Soda.setText("")
        self.Soda.setPixmap(QtGui.QPixmap("soda.png"))
        self.Soda.setScaledContents(True)
        self.Soda.setObjectName("Soda")
        self.gridLayout_7.addWidget(self.Soda, 0, 1, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")

        self.Water = QtWidgets.QLabel(self.layoutWidget)
        self.Water.setMinimumSize(QtCore.QSize(171, 181))
        self.Water.setText("")
        self.Water.setPixmap(QtGui.QPixmap("water.png"))
        self.Water.setScaledContents(True)
        self.Water.setObjectName("Water")
        self.gridLayout_8.addWidget(self.Water, 0, 0, 1, 1)

        self.tea2 = QtWidgets.QLabel(self.layoutWidget)
        self.tea2.setMinimumSize(QtCore.QSize(171, 181))
        self.tea2.setText("")
        self.tea2.setPixmap(QtGui.QPixmap("atai.png"))
        self.tea2.setScaledContents(True)
        self.tea2.setObjectName("tea2")
        self.gridLayout_8.addWidget(self.tea2, 0, 1, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.commandLinkButton.setText(_translate("Dialog", "Imprimer"))

class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, waiter_name):
        super(MyDialog, self).__init__()
        self.setupUi(self)
        self.waiter_name = waiter_name  # Set the waiter_name attribute
        self.item_prices = {"Tea": 7.00, "Caffe Creme": 10.00, "Chocolat Chaud": 10.00, "Noire": 7.00, "Ftour": 25.00, "Soda": 10.0, "Water": 2.00, "Tea 2": 7.00}
        self.total = 0.0
        self.receipt_id_counter = 0  # Counter for receipt ID
        self.receipts_today = self.get_receipts_count()  # Counter for receipts generated today
        self.total_prices = []  # List to store total prices of receipts

        # Initialize total of totals from recette.txt if it exists
        self.total_of_totals = self.initialize_total_of_totals()

        # Set up the header information
        self.date_time_label.setText(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.waiter_label.setText("Waiter: " + waiter_name)

        # Create a total label for the commandLinkButton
        self.total_label_command = QtWidgets.QLabel(self.commandLinkButton)
        self.total_label_command.setGeometry(QtCore.QRect(10, 30, 200, 30))
        self.total_label_command.setObjectName("total_label_command")
        self.total_label_command.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.total_label_command.setFont(QtGui.QFont("Arial", 14, weight=QtGui.QFont.Weight.Bold))

        # Set initial total text for the commandLinkButton
        self.total_label_command.setText("Total: 0.00 MAD")

        # Connect the mousePressEvent for each item
        self.Tea.mousePressEvent = lambda event: self.on_label_clicked("Tea")
        self.caffe_creme.mousePressEvent = lambda event: self.on_label_clicked("Caffe Creme")
        self.chocolat_chaud.mousePressEvent = lambda event: self.on_label_clicked("Chocolat Chaud")
        self.noire.mousePressEvent = lambda event: self.on_label_clicked("Noire")
        self.ftour.mousePressEvent = lambda event: self.on_label_clicked("Ftour")
        self.Soda.mousePressEvent = lambda event: self.on_label_clicked("Soda")
        self.Water.mousePressEvent = lambda event: self.on_label_clicked("Water")
        self.tea2.mousePressEvent = lambda event: self.on_label_clicked("Tea 2")


        # Show the dialog in fullscreen
        self.showFullScreen()

    def get_receipts_count(self):
        # Get the receipts count of the day from the receipts folder
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        receipts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Receipts", current_date)
        if os.path.exists(receipts_folder):
            return len([name for name in os.listdir(receipts_folder) if os.path.isfile(os.path.join(receipts_folder, name))])
        else:
            return 0

    def on_label_clicked(self, item_name):
        # Get the price of the selected item
        item_price = self.item_prices.get(item_name, 0.0)
        self.total += item_price

        # Add the selected item to the list widget
        item_text = f"{item_name}: {item_price:.2f} MAD"
        item = QtWidgets.QListWidgetItem(item_text)
        item.setFont(QtGui.QFont("Arial", 10, weight=QtGui.QFont.Weight.Bold))  # Set font size and weight
        self.listWidget.addItem(item)

        # Create and add the remove button (X icon) to the list widget item
        remove_button = QtWidgets.QLabel(" X")
        remove_button.setStyleSheet("color: red;")
        remove_button.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTop)
        remove_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        remove_button.setMinimumSize(QtCore.QSize(30, 30))  # Set a minimum size for the remove button
        remove_button.setContentsMargins(0, -5, 0, 0)  # Adjust margin to move the X up
        remove_button.setFont(QtGui.QFont("Arial", 14, weight=QtGui.QFont.Weight.Bold))  # Set bold font
        self.listWidget.setItemWidget(item, remove_button)

        # Connect the remove button to remove the item from the list widget
        remove_button.mousePressEvent = lambda event: self.on_remove_clicked(item, item_price)

        # Update total text for the commandLinkButton
        self.total_label_command.setText(f"Total: {self.total:.2f} MAD")

    def on_remove_clicked(self, item, item_price):
        # Remove the selected item from the list widget
        self.listWidget.takeItem(self.listWidget.row(item))

        # Subtract the price of the removed item from the total
        self.total -= item_price

        # Update total text for the commandLinkButton
        self.total_label_command.setText(f"Total: {self.total:.2f} MAD")

    def initialize_total_of_totals(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        receipts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Receipts", current_date)
        recette_filename = os.path.join(receipts_folder, 'recette.txt')
        if os.path.exists(recette_filename):
            with open(recette_filename, 'r') as file:
                existing_total = float(file.read().strip())
                return existing_total
        return 0.0

    def show_total(self):
        QtWidgets.QMessageBox.information(self, "Total of Totals", f"The total of totals is: {self.total_of_totals:.2f} MAD")

    def generate_receipt_text(self):
        try:
            self.receipt_id_counter += 1
            self.receipts_today += 1
            receipt_id = str(self.receipt_id_counter).zfill(3)
            company_name = "CAFE ROMA"
            company_address = "Al Amal DAR 16"
            company_city = "CASABLANCA"
            message = "Merci."

            # Get items from the list widget
            items = []

            for index in range(self.listWidget.count()):
                item_text = self.listWidget.item(index).text()
                item_name, item_price_str = item_text.split(":")
                item_price = float(item_price_str.strip().split()[0])
                items.append((item_name.strip(), item_price))
            
            total = sum(item[1] for item in items)
            self.total_prices.append(total)
            total_of_totals = sum(self.total_prices)

            # Get current date and time
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.datetime.now().strftime("%H-%M-%S")
            receipts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Receipts", current_date)
            if not os.path.exists(receipts_folder):
                os.makedirs(receipts_folder)

            # Generate receipt text file
            text_filename = os.path.join(receipts_folder, f"receipt_{receipt_id}_{current_time}.txt")

            with open(text_filename, "w") as file:
                file.write("*"*50 + "\n")
                file.write(f"\t\t{company_name.title()}\n")
                file.write(f"\t\t{company_address}\n")
                file.write(f"\t\t{company_city}\n\n")
                file.write(f"\tServeur: {self.waiter_name}\n\n")  # Include waiter name in receipt
                file.write(f"La date: {current_date} {current_time}\n")
                file.write(f"\t\t\t\t Reçu n°: {receipt_id}\n")
                file.write("*"*50 + "\n\n")
                file.write("\tProduct Name\tProduct Price\n\n")
                for item in items:
                    file.write(f"\t{item[0].title()}\t\t{item[1]} MAD\n")
                file.write("="*50 + "\n\n")
                total = sum(item[1] for item in items)
                file.write(f"\tTotal: {total} MAD\n\n")
                file.write("="*50 + "\n\n")
                file.write(f"\t\t{message.title()}\n\n")
                file.write("*"*50 + "\n")

            self.total_prices.append(total)  # Add total to total prices list
            total_of_totals = sum(self.total_prices)  # Calculate the total of totals
            self.print_receipt(text_filename)

            # Clear the list widget after generating the receipt
            self.listWidget.clear()

            # Reset the total value to 0 after printing the receipt
            self.total = 0.0
            self.total_label_command.setText(f"Total: {self.total:.2f} MAD")

            # Save the total of totals in the receipt folder
            self.save_total_of_totals(receipts_folder, total_of_totals)

        except Exception as e:
            self.log_error(e)


    def print_receipt(self, filename):
        # Try printing the receipt
        try:
            # Open the file for reading
            with open(filename, "r") as file:
                text = file.read()
            
            # Use subprocess to print the file
            subprocess.Popen(["notepad.exe", "/p", filename], shell=True)

            # Update the receipt count label
            self.receipt_count_label.setText(f"Receipts Today: {self.receipts_today}")

        except Exception as e:
            self.log_error(e)

    def log_error(self, error_message):
        # Log the error message to the exit log file
        log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LOG")
        log_filename = os.path.join(log_folder, f"exit_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(log_filename, 'a') as log_file:
            log_file.write(str(error_message) + '\n')

    def save_total_of_totals(self, folder_path, total_of_totals):
        # Save the total of totals in a text file named 'recette.txt' in the receipt folder
        recette_filename = os.path.join(folder_path, 'recette.txt')
        try:
            # If the recette.txt already exists, read its content and update the total of totals
            if os.path.exists(recette_filename):
                with open(recette_filename, 'r') as file:
                    existing_content = file.read().strip()
                # Convert existing content to float and add the new total of totals
                existing_total = float(existing_content)
                total_of_totals += existing_total
            # Write the new total of totals to the recette.txt file
            with open(recette_filename, 'w') as file:
                file.write(f"{total_of_totals:.2f}")
        except Exception as e:
            self.log_error(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_dialog = LoginDialog()
    if login_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
        dialog = MyDialog(login_dialog.waiter_name)
        dialog.show()
        sys.exit(app.exec())
