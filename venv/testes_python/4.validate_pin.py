def validate_pin(pin):
    #return true or false
    if not pin.isnumeric():
        return False
    
    if len(pin) != 4 and len(pin) != 6:
        return False
    
validate_pin("1234")