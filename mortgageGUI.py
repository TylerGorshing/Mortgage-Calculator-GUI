from tkinter import *
from tkinter import ttk

# The Mortgage Calculator code.


def calculate():
    loan_ammount = float(loan.get().replace(',', ''))
    interest_rate = float(rate.get()) / 100
    loan_term = float(term.get())
    yearly_payments = 12.0
    extra_payment = float(extraPayment.get())

    monthly_interest_rate = interest_rate / yearly_payments
    total_payment_number = loan_term * yearly_payments

    monthly_payment = loan_ammount * ((interest_rate / yearly_payments) / (
        1 - (1 + interest_rate / yearly_payments)**(-1 * yearly_payments * loan_term)))
    total_payment = monthly_payment * total_payment_number
    expect_interest = total_payment - loan_ammount
    monthly_payment += extra_payment

    if extra_payment == 0:

        monthlyPayment.set('${:,.2f}'.format(monthly_payment))
        totalPayment.set('${:,.2f}'.format(total_payment))
        totalInterest.set('${:,.2f}'.format(expect_interest))
        interestPaid.set('${:,.2f}'.format(expect_interest))
        interestSaved.set('$0')

    else:
        remaining_principle = loan_ammount
        payments = 0
        total_interest = 0

        while remaining_principle + (remaining_principle * monthly_interest_rate) > monthly_payment:
            month_interest = remaining_principle * monthly_interest_rate
            total_interest += month_interest
            to_principle = monthly_payment - month_interest
            remaining_principle += -1 * to_principle
            payments += 1

        month_interest = remaining_principle * monthly_interest_rate
        total_interest += month_interest

        total_payment = monthly_payment * payments + \
            month_interest + remaining_principle

        monthlyPayment.set('${:,.2f}'.format(monthly_payment))
        totalPayment.set('${:,.2f}'.format(total_payment))
        totalInterest.set('${:,.2f}'.format(total_interest))
        interestPaid.set('${:,.2f}'.format(total_interest))
        interestSaved.set('${:,.2f}'.format(expect_interest - total_interest))


# The GUI Code:

# Setting up the Window.

root = Tk()
root.title('Mortgage Calculator')

loan = StringVar()
rate = StringVar()
term = StringVar()
payment = StringVar()
extraPayment = StringVar()

monthlyPayment = StringVar()
totalPayment = StringVar()
totalInterest = StringVar()
interestPaid = StringVar()
interestSaved = StringVar()


root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# The window is divided into two halves left and right.

leftFrame = ttk.Frame(root)
leftFrame.grid(column=0, row=0, sticky='news')

rightFrame = ttk.Frame(root, width='10i')
rightFrame.grid(column=1, row=0, sticky='news')

#leftFrame.columnconfigure(0, weight=1)
leftFrame.rowconfigure(0, weight=0)
leftFrame.rowconfigure(1, weight=1)

# will need this when adding the right frame.
# rightFrame.columnconfigure(0, weight=1)
# rightFrame.rowconfigure(0, weight=1)

# The left frame is where all the information will be entered and the calculate button.

# The top half of the left frame has labels on the left and text entry on the right.

leftTopFrame = ttk.Frame(leftFrame)
leftTopFrame.grid(column=0, row=0, sticky='n')

# Labels on the left:


loanLabel = ttk.Label(leftTopFrame, text='Loan Amount:')
rateLabel = ttk.Label(leftTopFrame, text='Interest Rate (as a Percent):')
termLabel = ttk.Label(leftTopFrame, text='Term (in Years):')
#paymentLabel = ttk.Label(leftTopFrame, text='Payments per Month:')
extraPaymentLabel = ttk.Label(leftTopFrame, text='Extra Payment Amount:')

loanLabel.grid(column=0, row=0, sticky='w', padx=5, pady=5)
rateLabel.grid(column=0, row=1, sticky='w', padx=5, pady=5)
termLabel.grid(column=0, row=2, sticky='w', padx=5, pady=5)
#paymentLabel.grid(column=0, row=3, sticky='w', padx=5, pady=5)
extraPaymentLabel.grid(column=0, row=3, sticky='w', padx=5, pady=5)

# Text entry boxes on the right:


loanEntry = ttk.Entry(leftTopFrame, textvariable=loan, width=10)
rateEntry = ttk.Entry(leftTopFrame, textvariable=rate, width=10)
termEntry = ttk.Entry(leftTopFrame, textvariable=term, width=10)
#paymentEntry = ttk.Entry(leftTopFrame, textvariable=payment, width=10)
extraPaymentEntry = ttk.Entry(
    leftTopFrame, textvariable=extraPayment, width=10)

loanEntry.grid(column=1, row=0, sticky='e', padx=5)
rateEntry.grid(column=1, row=1, sticky='e', padx=5)
termEntry.grid(column=1, row=2, sticky='e', padx=5)
#paymentEntry.grid(column=1, row=3, sticky='e', padx=5)
extraPaymentEntry.grid(column=1, row=3, sticky='e', padx=5)


# Calculate button on the bottom of the left half of the window.

leftBottomFrame = ttk.Frame(leftFrame)
leftBottomFrame.grid(column=0, row=1, sticky='n')

calculateButton = ttk.Button(
    leftBottomFrame, text='Calculate', command=calculate)
calculateButton.grid(column=0, row=0, sticky='n', pady=5)

# The right frame presents all the calculated information.

# The top half of the right frame has the monthly payment, total payment for the life of the loan, and total interest paid.
# Labels on the right of the top half of the right frame are permanent and tell the user what information is being shown.

# This frame adds some width to the window.
ttk.Frame(rightFrame, width='4i').grid(column=0, row=0)

rightTopFrame = ttk.Frame(rightFrame)
rightTopFrame.grid(column=0, row=1, sticky='nw')

# The permanent labels on the right:

ttk.Label(rightTopFrame, text='Monthly Payment:').grid(
    column=0, row=0, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, text='Total Payment:').grid(
    column=0, row=1, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, text='Total Interest:').grid(
    column=0, row=2, sticky='w', padx=5, pady=5)
#ttk.Label(rightTopFrame, text='Interest Paid:').grid(column=0, row=3, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, text='Interest Saved:').grid(
    column=0, row=3, sticky='w', padx=5, pady=5)


ttk.Label(rightTopFrame, textvariable=monthlyPayment).grid(
    column=1, row=0, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, textvariable=totalPayment).grid(
    column=1, row=1, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, textvariable=totalInterest).grid(
    column=1, row=2, sticky='w', padx=5, pady=5)
#ttk.Label(rightTopFrame, textvariable=interestPaid).grid(column=1, row=3, sticky='w', padx=5, pady=5)
ttk.Label(rightTopFrame, textvariable=interestSaved).grid(
    column=1, row=3, sticky='w', padx=5, pady=5)


# The bottom half of the right side will contain a scroll bar to display specific payment information.

rightBottomFrame = ttk.Frame(rightFrame)
rightBottomFrame.grid(column=0, row=2, sticky='nw')


root.mainloop()
