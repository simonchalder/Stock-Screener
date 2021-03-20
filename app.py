# Imports
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
import stock

# 

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Stock Screener")

        # Set layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Title label

        title_label = qtw.QLabel("Stock Screener")
        title_label.setFont(qtg.QFont('Helvetica', 18)) # Change font
        self.layout().addWidget(title_label)

        # Stock Code Entry Box

        code_entry = qtw.QLineEdit()
        code_entry.setObjectName("code_input")
        self.layout().addWidget(code_entry)

        # Text Outputs

        name_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(name_output)

        cap_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(cap_output)

        cap_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(cap_output)

        debt_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(debt_output)

        peRatio_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(peRatio_output)

        eps_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(eps_output)

        cash_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(cash_output)

        borrowings_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(borrowings_output)

        shEquity_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(shEquity_output)

        profit_output = qtw.QTextEdit(self, readOnly = True)
        self.layout().addWidget(profit_output)

        # Submit Button

        submitButton = qtw.QPushButton("Submit", clicked = lambda: submitButtonClick())
        self.layout().addWidget(submitButton)


        # Row Allocation

        form_layout.addRow(title_label)
        form_layout.addRow("Enter Company Code: ", code_entry)
        form_layout.addRow("Name", name_output)
        form_layout.addRow("MCap", cap_output)
        form_layout.addRow("Debt", debt_output)
        form_layout.addRow("PE Ratio", peRatio_output)
        form_layout.addRow("EPS", eps_output)
        form_layout.addRow("Cash", cash_output)
        form_layout.addRow("Borrowings", borrowings_output)
        form_layout.addRow("SH Equity", shEquity_output)
        form_layout.addRow("Profit", profit_output)
        form_layout.addRow(submitButton)


        self.show()

        # Define functions after show()

        def submitButtonClick():
            code = code_entry.text()
            newStock = stock.Stock(code)

            name_output.setText(newStock.name)
            cap_output.setText(str(newStock.cap))
            debt_output.setText(str(newStock.debt))
            peRatio_output.setText(str(newStock.peRatio))
            eps_output.setText(str(newStock.eps))
            cash_output.setText(str(newStock.cash))
            shEquity_output.setText(str(newStock.shareholder_equity))
            profit_output.setText(str(newStock.annual_profits))
            newStock.assessStock()
            print(newStock.score)

app = qtw.QApplication([])

mw = MainWindow()

app.exec_()

