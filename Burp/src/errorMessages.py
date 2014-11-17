def ERROR001(nm):
	error_message = 'ERROR 001: Could not create the relation ' + nm + ' '
	error_message += 'due to model inconsistencies.' + '\n'
	error_message += 'The length of types must be the same length of attributes.'
	return error_message

def ERROR002(nm, missed_data, expected_value, received_value):
	error_message = 'ERROR 002: Could not insert value to the relation ' + nm + ' due to model '
	error_message += 'inconsistencies.' + '\n'
	error_message += 'Error inserting ' + missed_data + '. ' + '\n'
	error_message += 'Expected type is: ' + expected_value + '. Received type is: ' + received_value
	return error_message

def ERROR003(nm, data):
	error_message = 'ERROR 003: Could not insert value to the relation ' + nm + ' due to model '
	error_message += 'inconsistencies.' + '\n'
	error_message += 'The value ' + data + ' is present in the relation.'
	return error_message

def ERROR004(nm, expected, received):
	error_message = 'ERROR004: Could not insert value to the relation ' + nm + ' due to model '
	error_message += 'inconsistencies.' + '\n'
	error_message += 'The length of the tuple must be the same of the columns. '
	error_message += "Expected length: " + expected
	error_message += ". Received length: " + received
	return error_message

def ERROR005(nm, expected, received):
	error_message = 'ERROR005: Could not create new relation ' + nm + ' due to model '
	error_message += 'inconsistencies.' + '\n'
	error_message += 'The domains of each columns must be the same. '
	error_message += "Expected domain: " + expected
	error_message += ". Received domain: " + received
	return error_message

def ERRO6006(att, nm):
	error_message = 'ERROR006: Could not create projection on ' + nm + ' due to model '
	error_message += 'inconsistencies.' + '\n'
	error_message += 'The attibute ' + att + ' is not in the relation.'
	return error_message


