# GDPR Mask

**This kata requires knowledge of decorators.**

You are working on a customer and stock application. The application has a number of functions that produce responses for an API. These responses sometimes include personally identifiable information (PII) which cannot be exposed to certain users under GDPR regulation. You are required to write a _decorator_ (called `mask`) that can be applied to these functions to obscure personal data. The user should be able to specify which fields to obscure.

For example:
```python
@mask('name', 'email', 'mobile')
def get_client_details():
    return {
        'name': 'Jane Smith',
        'email': 'jane@coolmail.com',
        'telephones': {
            'mobile': '07999 987654'
        },
        'status': 'excellent'
    }
```

When we call `get_client_details`, we should see:
```python
{
        'name': '**** *****',
        'email': '*****************',
        'telephones': {
            'mobile': '***** ******'
        },
        'status': 'excellent'
}
```

The rules for obscuring are:
1. All characters except spaces should be replaced by '*'.
1. Fields not specified in the decorator arguments should be left unchanged.
1. All fields matching a specified field at any level of nesting should be changed. (In the example shown, specifying 'mobile' is enough to match 'telephones.mobile'.)

Please complete the code in the file `gdpr_mask.py`, writing tests as usual. When you are done, you should be able to run:
```bash
python src/gdpr_mask/api_response.py
```
You should see correctly masked data.
