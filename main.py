event_options = [
  {'name': 'wedding', 'rate': 400},
  {'name': 'club', 'rate': 450},
  {'name': 'concert', 'rate': 500},
  {'name': 'party', 'rate': 300}
]

addon_options = [
  {'name': 'audioequipt', 'fee': 300},
  {'name': 'lighteffects', 'fee': 300}
]

promocode_options = [
  {'name': 'boombox', 'value': 100},
]

def quotegen(event_type, event_length, selected_addons, promo_code):
    """
    Calculate event quote based on event type, event length, addons, and promo code.
    Returns the event quote as a string.
    """
    try:
        # Check if event type is valid
        if event_type not in [event_option['name'] for event_option in event_options]:
            raise ValueError("Invalid event type provided.")

        # Check if event length is a positive integer
        if not isinstance(event_length, int) or event_length <= 0:
            raise ValueError("Invalid event length provided.")

        # Check if selected addons are valid
        available_addons = [addon_option['name'] for addon_option in addon_options]
        invalid_addons = [addon for addon in selected_addons if addon not in available_addons]
        if invalid_addons:
            raise ValueError(f"Invalid addons provided: {', '.join(invalid_addons)}")

        # Check if promo code is valid
        available_promo_codes = [promocode_option['name'] for promocode_option in promocode_options]
        if promo_code not in available_promo_codes:
            raise ValueError("Invalid promo code provided.")

        # Calculate base event charge
        event_charge = next((event_option['rate'] for event_option in event_options if event_option['name'] == event_type), 0)
        total = event_charge * event_length
        
        # Calculate addon charges
        addon_fees = {addon_option['name']: addon_option['fee'] for addon_option in addon_options}
        total += sum(addon_fees.get(addon, 0) for addon in selected_addons)
        
        # Apply promo code
        promo_value = next((promocode_option['value'] for promocode_option in promocode_options if promocode_option['name'] == promo_code), 0)
        total -= promo_value
        # Format and return the result
        return f'Your total is ${total}.'
    except StopIteration:
        raise ValueError("Invalid input provided.")


try:
    result = quotegen('wedding', 8, ['audioequipt', 'lighteffects'], 'boombox')
    print(result)
except ValueError as e:
    print(f"Error: {str(e)}")