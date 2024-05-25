# Author: Dhaval Patel. Codebasics YouTube Channel

import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pandeyji_eatery"
)

# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()

        # Calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result

# Function to get the next available order_id
def get_next_order_id():
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None
    
def get_food_prices(names):

    # Create cursor
    cursor = cnx.cursor()

    # Prepare query
    query = "SELECT name, price FROM food_items WHERE name IN (%s)"
    placeholders = ', '.join(['%s'] * len(names))
    query = query % placeholders

    # Execute query
    cursor.execute(query, names)

    # Fetch results
    results = cursor.fetchall()

    # Close cursor and connection
    cursor.close()

    #Create dictionary with name as key and price as value
    price_dict = {}
    for row in results:
       price = int(row[1]) if isinstance(row[1], int) else float(row[1])
       price_dict[row[0].lower()] = price
    return price_dict
    #prices = [int(row[1]) if isinstance(row[1], int) else float(row[1]) for row in results]
    #return prices


def display_food_items_price():
    cursor = cnx.cursor()
    query = "SELECT name, price FROM food_items"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    # Format records into a single string
    display_string = ", ".join([f"{name}: ${price}" for name, price in records])
    return display_string

def display_food_items():
    cursor = cnx.cursor()
    query = "SELECT name FROM food_items"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    # Format records into a single string
    display_string = ", ".join([f"{name[0]}" for name in records])
    return display_string





if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    #print(get_next_order_id())
    # Example usage
    #food_names = ["samosa", "pizza"]
    #price_dict = get_food_prices(food_names)
    #print(price_dict)
    food_items_string = display_food_items()
    print(food_items_string)
