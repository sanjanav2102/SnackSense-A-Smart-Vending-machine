# Vending Machine System - DSA Based Python Project

## 📌 Overview

This is a **DSA-focused Python project** simulating a smart vending machine system. It emphasizes practical applications of **Object-Oriented Programming (OOP)** and core **Data Structures** to manage:

- Product inventory
- Sales and transaction tracking
- Graph-based navigation between machines
- Shortest path computation using **Dijkstra’s Algorithm**

The system offers two main user roles: **Admin** and **Customer**. Each role can perform specific actions like restocking, purchasing products, viewing sales, and navigating between vending machines.

---

## 🧠 Concepts Explored

### ✅ Object-Oriented Programming (OOP)
- **Classes & Objects**: Encapsulated entities like `Product`, `VendingMachine`, and `Transaction`.
- **Encapsulation**: Internal state managed via class methods.
- **Modularity**: Easy to expand features using well-defined objects.

### ✅ Data Structures Used
| Data Structure | Purpose |
|----------------|---------|
| **Dictionary (`dict`)** | To store product info (ID → `Product`), machine inventory, and graph adjacency list. |
| **List (`list`)** | To keep logs of transactions and sales history. |
| **Tuple** | Used in edge weights (for graph) and product-location lookups. |
| **Priority Queue / `heapq`** | For Dijkstra’s algorithm to find the shortest path efficiently. |
| **Set** | To track visited nodes in pathfinding. |

---

## 📦 Features

### Admin Features
- Add or remove vending machines
- Add/update/remove products in machines
- View complete transaction history
- Check top-selling products

### Customer Features
- Browse available products
- Find nearest machine with required product using **shortest path**
- Purchase a product (stock updates automatically)

---

## 🗺️ Graph and Shortest Path
- **Graph Representation**: The vending machines are treated as nodes; distances between them are weighted edges.
- **Dijkstra’s Algorithm** is used to compute the nearest vending machine from a customer's current location that has the product in stock.

---

## 🛠️ How to Run

1. Clone the repository or download the code.
2. Run the Python file:
   ```bash
   python vending_machine.py
