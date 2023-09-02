from src.gdpr_mask.gdpr_mask import mask

def test_should_return_input_unaltered_if_passed_no_arg():
    @mask()
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }
    output = get_client_details()
    expected = {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }
    assert output == expected

def test_should_return_masked_output_of_name():
    @mask('name')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }
    output = get_client_details()
    expected = {
            'name': '**** *****',
            'email': 'jane@coolmail.com',
            'telephones': {
                'mobile': '07999 987654'
            },
            'status': 'excellent'
        }
    assert output == expected

def test_should_return_masked_output_of_nested_item():
    @mask('mobile')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'test':{
                    'mobile': '07999 987654'
                }
            },
            'status': 'excellent'
        }
    output = get_client_details()
    expected = {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'test':{
                    'mobile': '***** ******'
                }
            },
            'status': 'excellent'
        }
    assert output == expected

def test_should_return_masked_output_of_nested_repeated_item():
    @mask('mobile')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'home':{'mobile': '07999 987654'},
                'work':{'mobile': '07934 378495'}
            },
            'status': 'excellent'
        }
    output = get_client_details()
    expected = {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'home':{'mobile': '***** ******'},
                'work':{'mobile': '***** ******'}
            },
            'status': 'excellent'
        }
    assert output == expected

def test_should_return_masked_output_of_multiple_items():
    @mask('name','mobile')
    def get_client_details():
        return {
            'name': 'Jane Smith',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'home':{'mobile': '07999 987654'},
                'work':{'mobile': '07934 378495'}
            },
            'status': 'excellent'
        }
    output = get_client_details()
    expected = {
            'name': '**** *****',
            'email': 'jane@coolmail.com',
            'telephones': { 
                'home':{'mobile': '***** ******'},
                'work':{'mobile': '***** ******'}
            },
            'status': 'excellent'
        }
    assert output == expected