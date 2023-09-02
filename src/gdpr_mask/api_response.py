# Do not change the code in this file
from datetime import datetime
from gdpr_mask import mask


@mask('customer_name', 'address_line_1',
      'address_line_2', 'post_code', 'telephone')
def get_product_history(product_code):
    return {
        'product_code': product_code,
        'number_in_stock': 14,
        'most_recent_purchase': {
                'customer_id': 1234,
                'number_purchased': 3,
                'customer_name': 'Robert De Niro',
                'address_line_1': '54 Acacia Avenue',
                'address_line_2': 'Didsbury',
                'city': 'Manchester',
                'post_code': 'M45 3PQ',
                'telephone': '0161 323 3434'
            }
    }


@mask('full_name', 'address_1', 'postal_code', 'mobile', 'primary_email')
def get_customer_profile(customer_number):
    return {
        'customer_number': customer_number,
        'customer_purchase_points': 73,
        'customer_joined': datetime(2019, 7, 23),
        'number_of_purchases': 43,
        'customer_details': {
            'customer_identifiers': {
                'full_name': 'Roger Hammerstein',
                'title': 'Lord',
                'gender': 'male'
            },
            'customer_location': {
                    'location_type': 'primary_residence',
                    'address_1': '19 Smithington Drive',
                    'address_2': 'Cleethorpes',
                    'address_3': 'Lincolnshire',
                    'postal_code': 'DN35 1UV',
            },
            'telephone_numbers': {
                'mobile': '07777 777777'
            },
            'email': {
                'primary_email': 'big_roj@hammerste.in'
            }
        }
    }


if __name__ == '__main__':
    print(get_product_history('xyz'))
    print(get_customer_profile(123))
