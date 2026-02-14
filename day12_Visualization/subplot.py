import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
# Subplot 2: Line Plot (Trend Line)
plt.subplot(1, 2, 2)
plt.plot(categories, sales, marker='o')
plt.title("Sales Trend")
plt.xlabel("Category")
plt.ylabel("Sales")
# Prevent overlapping
plt.tight_layout()
# Show plot
plt.show()
