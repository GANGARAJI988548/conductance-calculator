# Current Divider Calculator

total_current = float(input("Enter total current (A): "))
r1 = float(input("Enter resistance R1 (Ω): "))
r2 = float(input("Enter resistance R2 (Ω): "))

current_r1 = total_current * r2 / (r1 + r2)
current_r2 = total_current * r1 / (r1 + r2)

print(f"Current through R1 = {current_r1:.4f} A")
print(f"Current through R2 = {current_r2:.4f} A")
