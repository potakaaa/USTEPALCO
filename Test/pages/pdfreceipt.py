import pdfkit
class PDF_receipt:
    def __init__(self, title, account_number, name, address, transaction_number, date, time, items):
        self.html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                }}
                .receipt {{
                    width: 500px;
                    margin: 0 auto;
                }}
                .header {{
                    text-align: center;
                    font-size: 18px;
                    margin-bottom: 10px;
                    margin-top: 30px;
                }}
                .info {{
                    margin-bottom: 15px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 10px;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }}
                .total {{
                    margin-top: 10px;
                    font-weight: bold;
                    text-align: right;
                }}
            
            </style>
        </head>
        <body>
            <div class="receipt">
                <div class="header">
                    <h2>{title}</h2>
                </div>
                <div class="info">
                    <p><strong>Account Number:</strong> {account_number}</p>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Address:</strong> {address}</p>
                    <p><strong>Transaction Number:</strong> {transaction_number}</p>
                    <p><strong>Date:</strong> {date}</p>
                    <p><strong>Time:</strong> {time}</p>
                </div>
                <table>
                    <tr>
                        <th>Usage (kWh)</th>
                        <th>Cost per kWh</th>
                        <th>Amount (P)</th>
                    </tr>
                    {"".join(f'<tr><td>{item[0]}</td><td>{item[1]}</td><td>{item[2]}</td></tr>' for item in items)}
                </table>
                <div class="total">
                    <p>Total Amount: P {sum(item[2] for item in items):.2f}</p>
                </div>
            </div>
        </body>
        </html>
        """

    def generate(self, output_pdf_path):
        html_content = self.html_template
        options = {
            'page-size': 'A5',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
        }

        # Set the path to wkhtmltopdf executable
        pdfkit_config = pdfkit.configuration(wkhtmltopdf="D:\\Documents\SCHOOL WORKS\\1ST YEAR BS CS1A\\CS112 - Computer Programming 1\\Electric Billing System\\USTEPALCO-dev\\Test\\pages\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

        # Pass the configuration to pdfkit
        pdfkit.from_string(html_content, output_pdf_path, options=options, configuration=pdfkit_config)

if(__name__ == "__main__"):
    receipt_title = "Electric Bill Receipt"
    account_number = "6912345"
    name = "John Lloyd Arvin Bajolo"
    address = "149, Kalambaguhan Velez St."
    transaction_number = "69420"
    date = "1/17/2024"
    time = "4:45PM"

    # Sample items in the table (replace with your actual items)
    items = [
        (100, 0.15, 15.00),
        (150, 0.15, 22.50),
        # Add more items as needed
    ]

    # Generate HTML from receipt data
    output_file = ":\\Downloads"
    PDF_receipt(receipt_title, account_number, name, address, transaction_number, date, time, items).generate(output_file)


