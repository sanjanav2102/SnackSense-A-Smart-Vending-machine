"""overall Time Complexity:O(ElogV+MP+T)"""
"""E: Number of edges in the graph (connections between locations)
V: Number of vertices in the graph (locations)
M: Number of vending machines
P: Number of products per vending machine
T: Number of transactions in transaction history"""

class Product:
    """Class to represent a product in the vending machine."""
    #Time Complexity-O(1)
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name               # Name of the product
        self.price = price             # Price of the product
        self.quantity = quantity        # Current stock quantity
    #Time Complexity-O(1)
    def __str__(self):
        return f"{self.product_id}. {self.name} - ${self.price} (Qty: {self.quantity})"


class TransactionNode:
    """Node class for linked list to maintain transaction history."""
    #Time Complexity-O(1)
    def __init__(self, product_id, quantity):
        self.product_id = product_id  # ID of the dispensed product
        self.quantity = quantity        # Quantity dispensed
        self.next = None               # Pointer to the next node


class MinHeap:
    def __init__(self):
        self.heap=[] #Initialize an empty list to store heap elements

    def push(self, item):
        """Insert an item in min-heap"""
        self.heap.append(item)  #Add the item to the end of the heap
        self.bubble_up(len(self.heap) - 1) #bubble up to move the new element to correct place to maintain heap property

    def pop(self):
        """Remove and return the smallest item"""
        if len(self.heap) == 0:
            print("heap empty")  #when the heap is empty
            return
        if len(self.heap) == 1:
            return self.heap.pop()  #Return the only element if the heap has one item

        root = self.heap[0]  #Save the root element to return it later
        self.heap[0] = self.heap.pop()  #Move the last item to the root position and pop the minimum elemnt using recursion
        self.bubble_down(0)  #bubble down to move the new element to correct place to maintain heap property
        return root  # Return the original root

    def bubble_up(self, index):
        """Move the item at index up to its correct position."""
        parent_index = (index - 1) // 2  #Find the parent index
        while index > 0 and self.heap[index][0] <self.heap[parent_index][0]:
            #Swap if the current item is smaller than the parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index  #Move up the heap by making the current index as the parent index
            parent_index = (index - 1) // 2  #Update the parent index

    def bubble_down(self, index):
        """Move the item at index down to its correct position."""
        child_index = 2 * index + 1  #Left child index
        while child_index<len(self.heap):
            right_index = child_index + 1  #Right child index
            #Choose the smaller child to compare with
            if right_index<len(self.heap) and self.heap[right_index][0] <self.heap[child_index][0]:
                child_index = right_index
            if self.heap[child_index][0] <self.heap[index][0]:  #If child is smaller, swap
                self.heap[child_index], self.heap[index] = self.heap[index], self.heap[child_index]
                index = child_index  #Move down the heap by making the current index as theh child index
                child_index = 2 * index + 1  #Update child index
            else:
                break  #Stop if the heap property is restored

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0  # Return True if the heap has no elements

class TransactionHistory:
    """Class to represent transaction history using a linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
    #Time complexity: O(n)
    def add_transaction(self, product_id, quantity):
        """Add a transaction to the history."""
        new_transaction = TransactionNode(product_id, quantity)
        if not self.head:
            self.head = new_transaction
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_transaction
    #Time complexity: O(n)
    def get_recent_sales(self):
        """Get the list of recent sales from the transaction history."""
        sales = []
        current = self.head
        while current:
            sales.append((current.product_id, current.quantity))
            current = current.next
        return sales

class SalesStack:
    """Stack to keep track of sales for demand analysis."""
    def __init__(self):
        # Initialize an empty stack to keep track of product IDs sold.
        self.stack = []

    def push(self, product_id):
    
        self.stack.append(product_id)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):

        return len(self.stack) == 0

    def peek(self):

        if self.stack:
            return self.stack[-1]
        else:
            return None

    def get_demand_count(self, product_id):

        return self.stack.count(product_id)
    
class ProductNode:
    def __init__(self, product):
        self.product = product  # The Product object
        self.next = None  # Pointer to the next node


class ProductLinkedList:
    def __init__(self):
        self.head = None
    #Time Complexity: O(n)
    def add_product(self, product):
        new_node = ProductNode(product)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    #Time Complexity: O(n)
    def __iter__(self):
        current = self.head
        while current:
            yield current.product
            current = current.next

    #Time Complexity: O(n)
    def delete_product(self, name):
        current = self.head
        previous = None
        while current:
            if current.product.name.lower() == name.lower():
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return current.product
            previous = current
            current = current.next
        return None
    #Time Complexity: O(n)
    def find_product_by_id(self, product_id):
        current = self.head
        while current:
            if current.product.product_id == product_id:
                return current.product
            current = current.next
        return None
    #Time Complexity: O(n)
    def display_products(self):
        current = self.head
        while current:
            print(current.product)
            current = current.next

class VendingMachine:
    all_machines=[]
       #Time complexity: O(1)
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.products = ProductLinkedList()  # Linked list to store products
        self.transaction_history = TransactionHistory()  # Transaction history
        self.sales_stack = SalesStack()  # Stack for sales tracking
        VendingMachine.all_machines.append(self)
    #Time complexity: O(n)
    def add_product(self, product_id, name, price, quantity):
        if self.products.find_product_by_id(product_id):
            print(f"Product ID {product_id} already exists. Please enter a unique ID.")
            return
        product = Product(product_id, name, price, quantity)
        self.products.add_product(product)
        print(f"Product '{name}' added successfully with ID {product_id}.")
    def delete_product(self, name):
        """Admin deletes a product by name."""
        product = self.products.delete_product(name)
        if product:
            print(f"Product '{name}' deleted successfully.")
        else:
            print("Product not found.")
    def dispense_product(self, product_id, quantity):
        """Customer dispenses a specified quantity of a product."""
        product = self.products.find_product_by_id(product_id)

        if not product:
            print("Product not found.")
            return

        print(f"Found product: {product.name} with {product.quantity} available.")
        if product.quantity >= quantity:
            product.quantity -= quantity  
            self.transaction_history.add_transaction(product_id, quantity)  # Log the transaction
            self.sales_stack.push(product_id)  # Track the sale in the stack
            print(f"Dispensed {quantity} of '{product.name}', price: {quantity * product.price}.")
            self.check_restock(product)
        else:
            print(f"Insufficient quantity. Only {product.quantity} available.")
            if input(f"Do you want to purchase only {product.quantity}? (yes/no): ").strip().lower() == 'yes':
                quantity_dispensed = product.quantity
                product.quantity = 0
                self.transaction_history.add_transaction(product_id, quantity_dispensed)  # Log the transaction
                self.sales_stack.push(product_id)  # Track the sale in the stack
                print(f"Dispensed {quantity_dispensed} of '{product.name}', price: {quantity * product.price}.")
                self.check_restock(product)
            else:
                print("Transaction canceled.")


    def check_restock(self, product):
        if product.quantity < 5:  # Threshold for restocking
            # Get past quantities for the specified product ID
            past_quantities = [
                quantity for prod_id, quantity in self.transaction_history.get_recent_sales()
                if prod_id == product.product_id
            ]
            
            # Check for high demand and calculate total recent demand
            high_demand = any(quantity > 10 for quantity in past_quantities)  # O(m)
            demand_count = sum(past_quantities)  # O(m)

            # Determine restock quantity based on demand
            if high_demand:
                restock_quantity = 25
            elif demand_count > 19:
                restock_quantity = 15
            else:
                restock_quantity = 10

            # Update product quantity and log restocking
            product.quantity += restock_quantity
            print(f"'{product.name}' restocked by {restock_quantity}. New quantity: {product.quantity}")

    def display_products(self):
        print(f"\nProducts in Vending Machine {self.machine_id}:")
        self.products.display_products()


class Graph:
 
    def __init__(self):
        self.graph = {
            'l1': {'l2': 7, 'l5': 5},
            'l2': {'l1': 7, 'l3': 8},
            'l3': {'l2': 8, 'l4': 5},
            'l4': {'l3': 5, 'l5': 5},
            'l5': {'l1': 5, 'l4': 5}
        }

        self.vending_machines = {
            'v1': [('l1', 5), ('l4', 7), ('l5', 6)],
            'v2': [('l1', 3), ('l3', 8), ('l4', 5), ('l5', 4)],
            'v3': [('l2', 9), ('l3', 2), ('l4', 6)]
        }

        self.machine_objects = {
            'v1': self.create_vending_machine('v1', [
                (1, "Soda", 1.50, 10),
                (2, "Chips", 1.00, 15),
                (3, "Candy", 0.75, 20)
            ]),
            'v2': self.create_vending_machine('v2', [
                (3, "Candy", 0.75, 20),
                (4, "Juice", 2.00, 5),
                (6, "Gum", 0.50, 30)
            ]),
            'v3': self.create_vending_machine('v3', [
                (2, "Chips", 1.00, 15),
                (5, "Water", 1.00, 25),
                (6, "Gum", 0.50, 30)
            ])
        }

    def create_vending_machine(self, machine_id, products):
        vending_machine = VendingMachine(machine_id)
        for product in products:
                vending_machine.add_product(*product)
        return vending_machine

    def display_vending_machines(self):
        for machine_id, machine in self.machine_objects.items():
            print(f"\nVending Machine ID: {machine_id}")
            machine.display_products()

    
    # Dijkstra's algorithm to find the nearest vending machine with the specified product in stock.

    def find_nearest_vending_machine(self, start_location, product_id):

        # Set to keep track of visited locations to avoid reprocessing them.
        visited = set()

        # Min-heap to prioritize locations based on the shortest known distance from the start.
        min_heap = MinHeap()
        min_heap.push((0, start_location))  # Time Complexity: O(log V)

        # Variables to store the nearest machine and its distance if found.
        nearest_machine = None
        nearest_distance = float('inf')

        # Process locations by shortest distance until no more reachable locations.
        while not min_heap.is_empty():  # Time Complexity: O(V)
            # Pop the closest location from the min-heap.
            current_distance, current_location = min_heap.pop()  # Time Complexity: O(log V)

            # If this location has already been processed, skip it.
            if current_location in visited:
                continue
            visited.add(current_location)

            # Check if any vending machine at the current location has the specified product in stock.
            for machine, locs in self.vending_machines.items():  # Time Complexity: O(M)
                for loc, machine_distance in locs:  # Time Complexity: O(L), L = locations per machine
                    if current_location == loc:
                        # Check the list of products for the specified product ID.
                        product = next(
                            (p for p in self.machine_objects[machine].products if p.product_id == product_id), None
                        )  # Time Complexity: O(P)
                        
                        # If product is found and in stock, update nearest machine and distance if closer.
                        if product and product.quantity > 0:
                            total_distance = current_distance + machine_distance
                            if total_distance < nearest_distance:
                                nearest_distance = total_distance
                                nearest_machine = machine

            # Push neighboring locations with updated distances into the heap for further exploration.
            for adj_location, dist_to_adj in self.graph.get(current_location, {}).items():  # Time Complexity: O(A)
                if adj_location not in visited:
                    new_distance = current_distance + dist_to_adj
                    min_heap.push((new_distance, adj_location))  # Time Complexity: O(log V)

        # If no vending machine with the product was found, return None values.
        if nearest_machine is None:
            return None, None

        # Return the nearest machine and its distance.
        return nearest_machine, nearest_distance

class VendingMachineSystem:
   
    def __init__(self):
        self.graph = Graph()
        self.products = ProductLinkedList()
        self.machines = self.graph.machine_objects

    def run(self):
        while True:
            print("\nWelcome to the Vending Machine System")
            role = input("\n1.Admin\n2.customer\n3.Exit\nSelect role(1-3): ")
            if role == '1':
                self.admin_menu()
            elif role == '2':
                self.customer_menu()
            elif role == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")

    def admin_menu(self):
        """Menu for admin functionalities."""
        machine_id = input("Enter Vending Machine ID (v1/v2/v3): ").strip().lower()
        if machine_id not in self.graph.machine_objects:
            print("Invalid Vending Machine ID.")
            return

        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Delete Product")
            print("3. View Products")
            print("4. Exit Admin Menu")
            choice = input("Select an option (1-4): ").strip()

            if choice == '1':
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                id_exists = False
                for machine in VendingMachine.all_machines:
                    if machine != self:  # Skip the current machine
                        if machine.products.find_product_by_id(product_id):
                            id_exists = True
                            existing_product = machine.products.find_product_by_id(product_id)
                            if existing_product.name != name:
                                print(f"Product ID {product_id} with the different name  already exists in another vending machine.")
                                return  # Do not add the product

                
                
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                self.graph.machine_objects[machine_id].add_product(product_id, name, price, quantity)

            elif choice == '2':
                name = input("Enter Product Name to delete: ")
                self.graph.machine_objects[machine_id].delete_product(name)

            elif choice == '3':
                self.graph.machine_objects[machine_id].display_products()

            elif choice == '4':
                print("Exiting Admin Menu.")
                break
            else:
                print("Invalid option. Please choose again.")

                

    def customer_menu(self):
        """Menu for customer functionalities."""
        location = input("Enter your current location (l1, l2, l3, l4, l5): ").strip().lower()
        if location not in self.graph.graph.keys():
            print("The location entered is invalid.")
            return
    
        print("\nAll available products across vending machines:")
        for machine_id in self.graph.machine_objects:
            self.graph.machine_objects[machine_id].display_products()  # Display products in each machine

        product_id = int(input("Enter Product ID you want to buy: "))

        nearest_machine, distance = self.graph.find_nearest_vending_machine(location,product_id)

        if nearest_machine:
            print(f"The nearest vending machine is {nearest_machine} at a distance of {distance} units.")
            quantity = int(input("Enter quantity: "))  

        
            nearest_machine = self.graph.machine_objects[nearest_machine]

            success = nearest_machine.dispense_product(product_id, quantity)

        else:
            print("No available vending machine has the requested product.")



if __name__ == "__main__":
    system = VendingMachineSystem()
    system.run()
