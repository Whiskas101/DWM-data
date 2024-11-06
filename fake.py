







from faker import Faker
import pandas as pd 
import random

fake = Faker()

def generate_cust_data(filename, save = False,  path="./data"):
    cust_records = 100 
    cust_id = [x for x in range(1, cust_records + 1)] 
    cust_income_bracket = ["<10k", "20-50k","50-100k","100-150k",">200k"]
    
    print(cust_id)
    cust_columns = {
        "CustomerID": cust_id,
        "first_name":[fake.first_name() for cust in range(cust_records)],
        "last_name": [fake.last_name() for cust in range(cust_records)],
        "email": [ fake.email() for cust in range(cust_records)],
        "phone": [ fake.phone_number() for cust in range(cust_records)],
        "city": [ fake.city() for cust in range(cust_records)],
        "state": [ fake.state() for cust in range(cust_records)],
        "country": [ fake.country() for cust in range(cust_records)],
        "dob": [ fake.date_of_birth(minimum_age=18) for cust in range(cust_records)],
        "city": [ fake.city() for cust in range(cust_records)],
        "income": [ random.choice(cust_income_bracket) for cust in range(cust_records)],
    }

    data = pd.DataFrame(cust_columns)
    
    print(data)

    if(save):
        data.to_csv(f"{path}/{filename}")


generate_cust_data(filename="cust_data.csv",save=True)

def generate_products_data(filename, save=False, path="./data"):
        
    # Number of products to generate
    num_products = 100

    supplier_ids = list(range(1, 11))  
    store_ids = list(range(1, 21))     

    categories = {
        "Grocery": ["Fruits", "Vegetables", "Beverages", "Snacks"],
        "Apparel": ["Men's Clothing", "Women's Clothing", "Shoes", "Accessories"],
        "Electronics": ["Mobile", "Laptop", "Home Appliances", "Audio"],
    }

    products_data = {
        "ProductID": range(1, num_products + 1),  
        "ProductName": [fake.word().capitalize() + " " + fake.word().capitalize() for _ in range(num_products)],
        "Category": [],
        "SubCategory": [],
        "Brand": [fake.company() for _ in range(num_products)],
        "SupplierID": [random.choice(supplier_ids) for _ in range(num_products)],  
        "StoreID": [random.choice(store_ids) for _ in range(num_products)],  
        "ListPrice": [round(random.uniform(5, 500), 2) for _ in range(num_products)],  
        "DiscountRate": [round(random.uniform(0, 0.5), 2) for _ in range(num_products)],  
        "InventoryLevel": [random.randint(0, 200) for _ in range(num_products)],  
    }

    for _ in range(num_products):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])
        products_data["Category"].append(category)
        products_data["SubCategory"].append(subcategory)

    data = pd.DataFrame(products_data)
    print(data.head())


    if(save):
        data.to_csv(f"{path}/{filename}")


#generate_products_data(filename="products.csv", save=True)

# Theres 100 products, 20 stores, and 10 suppliers


def generate_stores_data(filename, save=False, path="./data"):
        # Number of stores
    num_stores = 20


    store_types = ["Supercenter", "Neighborhood Market", "Sam’s Club"]

    stores_data = {
        "StoreID": range(1, num_stores + 1),  # Primary Key
        "StoreName": [fake.company() + " Store" for _ in range(num_stores)],
        "Location": [fake.city() if random.choice([True, False]) else fake.state() for _ in range(num_stores)],
        "SquareFootage": [random.randint(5000, 50000) for _ in range(num_stores)],  # Random area in square feet
        "OpeningDate": [fake.date_this_century() for _ in range(num_stores)],  # Random date within this century
        "AverageCustomerFootfall": [random.randint(100, 5000) for _ in range(num_stores)],  # Random daily footfall
        "StoreType": [random.choice(store_types) for _ in range(num_stores)],  # Randomly chosen store type
    }

    data = pd.DataFrame(stores_data)

    data.to_csv("stores_mock_data.csv", index=False)
    print(data.head())


    if(save):
        data.to_csv(f"{path}/{filename}")

#generate_stores_data("store_data.csv", save=True)



def generate_order_data(filename, save=False, path="./data"):


    num_orders = 500  # Total number of unique orders
    num_order_details = 500  # Total number of order details across all orders


    customer_ids = list(range(1, 101))  # Assuming 100 customers
    store_ids = list(range(1, 21))  # 20 stores
    product_ids = list(range(1, 101))  # Assuming 100 products


    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Cash"]
    delivery_options = ["In-store Pickup", "Home Delivery"]


    data = {
        "OrderID": [],
        "CustomerID": [],
        "OrderDate": [],
        "StoreID": [],
        #"TotalAmount": [],
        "ShippingFee": [],
        "Tax": [],
        "PaymentMethod": [],
        "DeliveryOption": [],
        #"OrderDetailID": [],
        "ProductID": [],
        "Quantity": [],
        #"UnitPrice": [],
        "Discount": []
    }

# Counter for OrderDetailID
    #order_detail_id = 1


    for order_id in range(1, num_orders + 1):
        
        customer_id = random.choice(customer_ids)
        order_date = fake.date_this_year()
        store_id = random.choice(store_ids)
        payment_method = random.choice(payment_methods)
        delivery_option = random.choice(delivery_options)
        shipping_fee = round(random.uniform(5, 20), 2)
        tax = round(random.uniform(1, 15), 2)
        
        
        total_amount = 0

        
        num_items = random.randint(1, 5)
        for _ in range(num_items):
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 10)
            unit_price = round(random.uniform(10, 200), 2)
            discount = round(random.uniform(0, 0.3), 2)  # Discount between 0% and 30%

            
            line_total = quantity * unit_price * (1 - discount)
            total_amount += line_total

            
            data["OrderID"].append(order_id)
            data["CustomerID"].append(customer_id)
            data["OrderDate"].append(order_date)
            data["StoreID"].append(store_id)
            #data["TotalAmount"].append(None)  # Placeholder, will fill later
            data["ShippingFee"].append(shipping_fee)
            data["Tax"].append(tax)
            data["PaymentMethod"].append(payment_method)
            data["DeliveryOption"].append(delivery_option)
            #data["OrderDetailID"].append(order_detail_id)
            data["ProductID"].append(product_id)
            data["Quantity"].append(quantity)
            #data["UnitPrice"].append(unit_price)
            data["Discount"].append(discount)

            
            #order_detail_id += 1

        
        #total_order_amount = round(total_amount + shipping_fee + tax, 2)
        #for i in range(len(data["OrderID"])):
        #    if data["OrderID"][i] == order_id:
        #   data["TotalAmount"][i] = total_order_amount


    data = pd.DataFrame(data)


    print(data.head(10))



    if(save):
        data.to_csv(f"{path}/{filename}", index=False)


#generate_order_data("orders_data.csv", save=True)


def generate_supplier_data(filename, save = False,  path="./data"):

        

    num_suppliers = 10   


    suppliers_data = {
        "SupplierID": range(1, num_suppliers + 1),  # Primary Key
        "SupplierName": [fake.company() for _ in range(num_suppliers)],
        "ContactName": [fake.name() for _ in range(num_suppliers)],
        "ContactEmail": [fake.email() for _ in range(num_suppliers)],
        "Phone": [fake.phone_number() for _ in range(num_suppliers)],
        "City": [fake.city() for _ in range(num_suppliers)],
        "Country": [fake.country() for _ in range(num_suppliers)],
    }


    data = pd.DataFrame(suppliers_data)

    print(data.head())

    if(save):
        data.to_csv(f"{path}/{filename}", index=False)


#generate_supplier_data("supplier_data.csv", save=True)

def generate_employee_data(filename, save = False,  path="./data" ):
    num_employees = 100  # Adjust as needed


    departments = ["Sales", "Human Resources", "IT", "Marketing", "Customer Service", "Logistics"]
    positions = ["Manager", "Sales Associate", "Customer Support", "Warehouse Staff", "Marketing Specialist", "IT Technician"]


    employees_data = {
        "EmployeeID": range(0, num_employees ),  # Primary Key
        "FirstName": [fake.first_name() for _ in range(num_employees)],
        "LastName": [fake.last_name() for _ in range(num_employees)],
        "Position": [random.choice(positions) for _ in range(num_employees)],
        "Department": [random.choice(departments) for _ in range(num_employees)],
        "HireDate": [fake.date_this_decade() for _ in range(num_employees)],
        "Salary": [round(random.uniform(30000, 120000), 2) for _ in range(num_employees)],  # Random salary range
        "StoreID": [random.choice(range(1, 21)) for _ in range(num_employees)],  # Foreign Key to Stores
    }


    data = pd.DataFrame(employees_data)

    print(data.head())


    if(save):
        data.to_csv(f"{path}/{filename}", index=False)


#generate_employee_data("employee_data.csv", save=True)



