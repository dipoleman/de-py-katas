import re
class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def extract_domain_name(url):
    """
    Extracts the domain name from a given URL.

    This function uses a regular expression to extract the domain name 
    from a given URL. The regular expression matches the 
    `http://` or `https://` prefix, followed by an optional `www.` prefix, 
    and captures the domain name, which consists of one or more word characters 
    followed by a dot and a two- or three-letter top-level domain.

    Args:
        url (str): The URL to extract the domain name from.

    Returns:
        str: The extracted domain name.

    Raises:
        BadInputError: If the input URL is not a string or if no domain 
        name is found in the URL.
    """
    if not isinstance(url, str):
        raise BadInputError(f"Invalid input: {url} is not a string")

    regex = r"(?:https?:\/\/)(?:www\.)?([\w]+\.[a-z]{2,3})"
    match = re.search(regex, url)
    
    if not match:
        raise BadInputError(f"No domain name found in: {url}")

    return match.group(1)
