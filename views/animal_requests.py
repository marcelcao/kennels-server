import sqlite3
import json
from models import Animal
from models import Locations
from models import Customer

# ANIMALS = [
#     {
#         "id": 1,
#         "name": "Snickers",
#         "species": "Dog",
#         "locationId": 1,
#         "customerId": 4,
#         "status": "Admitted"
#     },
#     {
#         "id": 2,
#         "name": "Roman",
#         "species": "Dog",
#         "locationId": 1,
#         "customerId": 2,
#         "status": "Admitted"
#     },
#     {
#         "id": 3,
#         "name": "Blue",
#         "species": "Cat",
#         "locationId": 2,
#         "customerId": 1,
#         "status": "Admitted"
#     }
# ]

# Function with a single parameter
def get_single_animal(id):
    """Variable to hold a single animal if it exists"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.customer_id,
            a.status,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['customer_id'], data['status'], data['location_id'])

        return animal.__dict__

def create_animal(new_animal):
    """Creates a new animal"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, customer_id, status, location_id)
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['breed'],
              new_animal['customer_id'], new_animal['status'],
              new_animal['location_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal['id'] = id


    return new_animal

def delete_animal(id):
    """Function to delete an animal"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

def update_animal(id, new_animal):
    """Updates animal"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                customer_id = ?,
                status = ?,
                location_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['customer_id'], new_animal['status'],
              new_animal['location_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_all_animals():
    """Function to get all animals"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.customer_id pet_customer_id,
            a.status,
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.id customer_id,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM Animal a
        LEFT JOIN Location l
            ON l.id = a.location_id
        LEFT JOIN Customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'], row['customer_id'], row['status'], row['location_id'])
            
            # Create a Location instance from the current row
            location = Locations(row['id'], row['location_name'], row['location_address'])
            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password'])
            
            animal.location = location.__dict__
            animal.customer = customer.serialized()

            animals.append(animal.__dict__)

    return animals

def get_animal_by_location(location_id):
    """Query for customer email address"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.breed,
            c.customer_id,
            c.status,
            c.location_id
        from Animal c
        WHERE c.location_id = ?
        """, ( location_id, ))

        animal_located = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['customer_id'], row['status'], row['location_id'])
            animal_located.append(animal.__dict__)

    return animal_located

def get_animal_by_status(status):
    """Query for customer email address"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.breed,
            c.customer_id,
            c.status,
            c.location_id
        from Animal c
        WHERE c.status = ?
        """, ( status, ))

        animal_status = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['customer_id'], row['status'], row['location_id'])
            animal_status.append(animal.__dict__)

    return animal_status
