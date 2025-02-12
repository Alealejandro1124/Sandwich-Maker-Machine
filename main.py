### Data ###
"""
Edited by Alejandro Murillo on 02/11/2025:
- edited main function
- edited check_resources function
- edited process_coins function
- edited transaction_result function
- edite make_sandwich function
- edited SandwichMachine class
"""

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

"""
SandwichMachine class
- check_resources
- process_coins
- transaction_result
- make_sandwich
"""
class SandwichMachine:

    def __init__(self, machine_resources):

        """
        Initializes the SandwichMachine with the available resources.

        Args:
            machine_resources (dict): Dictionary of resources to initialize the machine with.
        """
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """
        Check if there are enough resources to make a sandwich.
        Compares the resources available in the machine with the required ingredients.

        Args: ingredients (dict): required ingredients for a sandwich.

        Returns: bool: True if there are enough resources, False otherwise.

        """
        # Loop through each ingredient required by the sandwich
        for item in ingredients:
            # If the available resource is less that the required amount
            if self.machine_resources.get(item, 0) < ingredients[item]:
                # print an error message and return false.
                print(f"There is not enough {item}.")
                return False
        # If all ingredients are available, return true.
        return True

    def process_coins(self):
        """
        Process coin input from the user and calculate the total amount inserted.

        Prompts the user to enter the number of coins for each type and calculates the total value.

        Returns:
            float: The total value of the coins inserted.
        """
        # Inform user to insert coins
        print("Please insert coins.")
        # Prompt for each type of coin, covert to integer
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        # Calculate the total monetary value based on coin denominations.
        total = large_dollars * 1.0 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
        return total


    def transaction_result(self, coins, cost):
        """
               Validate the transaction by comparing inserted coins to the cost of the sandwich.

               If the inserted amount is insufficient, the transaction fails and the user is notified.
               If sufficient, the change is calculated and displayed.

               Args:
                   coins (float): The total value of coins inserted.
                   cost (float): The cost of the sandwich.

               Returns:
                   bool: True if the transaction is successful, False otherwise.
               """
        # Check if the inserted coins are less than the cost.
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        # Calculate and round the change (even if it is $0.0).
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deduct the required ingredients from the machine's resources to make the sandwich.

        After a successful transaction, this method subtracts the used ingredients
        from the machine's current resource count and informs the user.

        Args:
            sandwich_size (str): The size of the sandwich (small, medium, or large).
            order_ingredients (dict): Dictionary containing the required ingredients and quantities.
        """
        # Loop through the required ingredients and deduct each from the resources.
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        # Notify the user that the sandwich is ready.
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

def main():
    """
    Main function used to run the SandwichMachine class.

    This function creates an instance of the SandwichMachine, prompts for user input,
    and then calls the make_sandwich method to do one of the following
    three options 1.) make a sandwich, if resources are available. 2.) show the resources. 3.) quit.
    """

    # Create an instance of SandwichMachine using the initial resources.
    machine = SandwichMachine(resources)

    while True:
        # Prompt the user for sandwich size or action
        choice = input("What would you like? (small, medium, large, off, report): ").lower()

        # If the user enters "off" exit the loop and end the program.
        if choice == "off":
            break

        # If the user enters "report", display available ingredients.
        elif choice == "report":
            print(f"Bread: {machine.machine_resources['bread']} slices(s)")
            print(f"Ham: {machine.machine_resources['ham']} slices(s)")
            print(f"Cheese: {machine.machine_resources['cheese']} ounces(s)")

        # If the user selects a valid sandwich size (small, medium, large)
        elif choice in recipes:
            recipe = recipes[choice]
            # check if there are enough resources to make selected sandwich size
            if not machine.check_resources(recipe["ingredients"]):
                continue # If resources are insufficient, return to start of loop.

            #Process the inserted coins
            #Used ChatGPT to debug code and fix an indentation error here
            coins = machine.process_coins()

            # Validate the transaction based on the coin total and the sandwich cost.
            if not machine.transaction_result(coins, recipe["cost"]):
                continue  # If the transaction fails, return to the start of the loop.

            # Deduct the ingredients and make the sandwich.
            machine.make_sandwich(choice, recipe["ingredients"])
        else:
            # If the user enters an invalid option, prompt them to enter a valid input.
            print("Invalid input. Please choose a valid option.")

# Run the main() function.
if __name__ == "__main__":
    main()