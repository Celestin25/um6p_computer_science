import random
import datetime
import hashlib

def generate_rra_receipt(customer_name, items):
    # 1. Standard RRA Headers
    tin = "100000123"  # Mock TIN
    mrc = "RRA-MOCK-DEV-01" # Machine Registration Code
    sdc = "SDC001234567" # Sales Data Controller ID
    
    # 2. Calculate Totals
    total_taxable_a = 0 # Exempt
    total_taxable_b = 0 # VAT 18%
    total_vat = 0
    total_amount = 0
    
    print("-" * 40)
    print("       RWANDA REVENUE AUTHORITY")
    print("          EBM v2 RECEIPT")
    print("-" * 40)
    print(f"MERCHANT:   MY CLIENT BUSINESS LTD")
    print(f"TIN:        {tin}")
    print(f"MRC:        {mrc}")
    print(f"CUSTOMER:   {customer_name}")
    print("-" * 40)
    
    # 3. List Items
    print(f"{'ITEM':<20} {'QTY':<5} {'PRICE':<8} {'TOTAL'}")
    
    for item in items:
        name = item['name']
        qty = item['qty']
        price = item['price']
        total = qty * price
        vat_rate = 0.18
        
        # Calculate VAT (Standard 18%)
        tax_amount = (total * vat_rate) / (1 + vat_rate)
        total_vat += tax_amount
        total_taxable_b += (total - tax_amount)
        total_amount += total
        
        print(f"{name:<20} {qty:<5} {price:<8} {total}")

    print("-" * 40)
    print(f"TOTAL EXCL. TAX:     {int(total_taxable_b)} RWF")
    print(f"TOTAL VAT (18%):     {int(total_vat)} RWF")
    print(f"TOTAL INCL. TAX:     {int(total_amount)} RWF")
    print("-" * 40)
    
    # 4. Generate the "Purchase Code" (Receipt Signature)
    # RRA uses a specific hash, usually usually simplified for display
    # Format: XXXX-XXXX-XXXX-XXXX
    raw_sig = f"{tin}{mrc}{datetime.datetime.now()}{total_amount}"
    hash_sig = hashlib.md5(raw_sig.encode()).hexdigest().upper()
    receipt_signature = f"{hash_sig[:4]}-{hash_sig[4:8]}-{hash_sig[8:12]}-{hash_sig[12:16]}"
    
    receipt_number = f"{random.randint(1000,9999)}/{random.randint(1000,9999)}"
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Receipt Item:      {len(items)}")
    print(f"Receipt No:        {receipt_number}")
    print(f"Date:              {date_time}")
    print(f"SDC ID:            {sdc}")
    print(f"RECEIPT SIGNATURE: {receipt_signature}")
    print("-" * 40)
    print("       INTERNAL DATA FOR VERIFICATION")
    print("-" * 40)
    
    return receipt_signature

# --- INPUT DATA ---
customer = "SCIENCES PO DEMO USER"
purchase_items = [
    {"name": "Consulting Svc", "qty": 1, "price": 50000},
    {"name": "Server Setup",   "qty": 2, "price": 150000},
    {"name": "Cables (m)",     "qty": 10, "price": 1000}
]

# --- RUN ---
code = generate_rra_receipt(customer, purchase_items)