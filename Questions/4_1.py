with open("stocks.csv", "r", encoding="utf-8") as f, open("output.csv", "w", newline="", encoding="utf-8") as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")  
    next(f)  # Skip header line
    
    for line in f:
        tokens = line.strip().split(",")  # Strip whitespace before splitting
        print(tokens)
        
        if len(tokens) != 4:  # Ensure correct number of columns
            continue  # Skip any malformed lines
        
        stock = tokens[0]
        
        try:
            price = float(tokens[1])
            eps = float(tokens[2])
            book = float(tokens[3])

            pe = round(price / eps, 2) if eps != 0 else "N/A"  # Avoid division by zero
            pb = round(price / book, 2) if book != 0 else "N/A"

            out.write(f"{stock},{pe},{pb}\n")
        
        except ValueError:
            print(f"Skipping invalid row: {tokens}")  # Handle invalid numeric values
