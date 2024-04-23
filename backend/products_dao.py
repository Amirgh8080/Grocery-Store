from sql_connection import get_sql_connection
from mysql import connector


def get_all_products(connection):

    cursor = connection.cursor()
    query = ('''SELECT product_id, name, price_per_unit, uom.uom_name FROM grocery_store.products 
                inner join grocery_store.uom on products.uom_id=uom.uom_id;''')
    response = []
    try:
        cursor.execute(query)

        # noinspection PyTypeChecker
        for (product_id, name, price_per_unit, uom_name) in cursor:
            response.append(
                {
                    'product_id': product_id,
                    'name': name,
                    'price_per_unit': price_per_unit,
                    'uom_name': uom_name
                }
            )

    except connector.Error as err:
        print(f"Error: {err}")

    return response


def insert_product(connection, product):

    query = ('''
            INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s);
            ''')
    data = [product['name'], product['uom_id'], product['price_per_unit']]

    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, product_id):
    query = "DELETE FROM products WHERE product_id=" + str(product_id)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))

