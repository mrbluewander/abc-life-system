
# txf_risk_calculator.py

def calculate_max_safe_contracts():
    # Get user input
    current_price = int(input("Enter Current Price: "))
    estimated_stop_loss_points = int(input("Enter Estimated Stop Loss Points: "))

    # Calculate max risk amount
    max_risk_amount = 600000 * 0.02

    # Calculate risk per contract
    risk_per_contract = estimated_stop_loss_points * 200

    # Calculate max contracts
    max_contracts = int(max_risk_amount / risk_per_contract)

    # Print report
    print("\nTXF Risk Calculator Report:")
    print(f"Current Price: {current_price}")
    print(f"Stop Loss Points: {estimated_stop_loss_points}")
    print(f"Max Risk Amount (NTD): {max_risk_amount:.2f}")
    print(f"Risk Per Contract (NTD): {risk_per_contract}")
    print(f"MAX SAFE CONTRACTS: {max_contracts}")

    # Print warning if max contracts is 0
    if max_contracts == 0:
        print("\nWARNING: Max Contracts is 0. Please review your stop loss points or max risk amount.")

if __name__ == "__main__":
    calculate_max_safe_contracts()
