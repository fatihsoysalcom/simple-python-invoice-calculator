import datetime

class Invoice:
    def __init__(self, invoice_number, customer_name):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.issue_date = datetime.date.today()
        self.items = []
        self.tax_rate = 0.18 # Example tax rate (e.g., KDV in Turkey)

    def add_item(self, description, quantity, unit_price):
        """Adds an item to the invoice."""
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if not isinstance(unit_price, (int, float)) or unit_price <= 0:
            raise ValueError("Unit price must be a positive number.")
        self.items.append({
            "description": description,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": quantity * unit_price
        })

    def calculate_subtotal(self):
        """Calculates the sum of all item line totals."""
        return sum(item["line_total"] for item in self.items)

    def calculate_tax_amount(self):
        """Calculates the tax amount based on the subtotal and tax rate."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_grand_total(self):
        """Calculates the grand total including tax."""
        return self.calculate_subtotal() + self.calculate_tax_amount()

    def generate_invoice_text(self):
        """Generates a formatted text representation of the invoice."""
        invoice_text = f"--- INVOICE #{self.invoice_number} ---\n"
        invoice_text += f"Customer: {self.customer_name}\n"
        invoice_text += f"Date: {self.issue_date.strftime('%Y-%m-%d')}\n"
        invoice_text += "-" * 50 + "\n"
        invoice_text += f"{'Description':<25} {'Qty':>5} {'Unit Price':>10} {'Total':>10}\n"
        invoice_text += "-" * 50 + "\n"
        for item in self.items:
            invoice_text += (
                f"{item['description']:<25} {item['quantity']:>5} "
                f"{item['unit_price']:>10.2f} {item['line_total']:>10.2f}\n"
            )
        invoice_text += "-" * 50 + "\n"
        subtotal = self.calculate_subtotal()
        tax_amount = self.calculate_tax_amount()
        grand_total = self.calculate_grand_total()
        invoice_text += f"{'Subtotal:':<37} {subtotal:>10.2f}\n"
        invoice_text += f"{f'Tax ({self.tax_rate*100:.0f}%):':<37} {tax_amount:>10.2f}\n"
        invoice_text += f"{'GRAND TOTAL:':<37} {grand_total:>10.2f}\n"
        invoice_text += "-" * 50 + "\n"
        invoice_text += "Thank you for your business!\n"
        return invoice_text

# --- Example Usage ---
if __name__ == "__main__":
    print("Demonstrating a simple invoice management system.\n")

    # Create a new invoice instance
    # This represents the core data structure for an invoice, a key part of "digitalization" in financial processes.
    invoice1 = Invoice("INV-2023-001", "Acme Corp.")
    print(f"Created invoice for {invoice1.customer_name} (Invoice #{invoice1.invoice_number})")

    # Add items to the invoice
    # Adding items and calculating totals programmatically helps "reduce errors" and improve "efficiency".
    invoice1.add_item("Product A", 2, 150.00)
    invoice1.add_item("Service B", 1, 500.00)
    invoice1.add_item("Consulting Hours", 5.5, 75.00)

    # Generate and print the invoice
    print("\n--- Generated Invoice ---")
    print(invoice1.generate_invoice_text())

    # Create another invoice to show reusability of the system
    invoice2 = Invoice("INV-2023-002", "Globex Inc.")
    invoice2.add_item("Software License", 1, 1200.00)
    invoice2.add_item("Support Package", 1, 200.00)

    print("\n--- Another Generated Invoice ---")
    print(invoice2.generate_invoice_text())

    print("Example complete. This script demonstrates basic invoice data handling and calculation.")
