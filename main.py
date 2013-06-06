import re


class PyForm:

	def add_rule(self, value, name, *ruleCheck):
		#ruleString can have | as delimiter for methods and [] for arguments for those methods
		rule = {}
		rule['value'] = value
		rule['name'] = name
		rule['checks'] = ruleCheck

		self.rules.append(rule)

	def run(self):
		self.log = {}
		valid = True

		for method in self.rules:
			self.log[ method['name'] ] = []

			for rules in method['checks']:
				for rule in rules:
					method_to_call = getattr(ValidationMethods, rule)
					validation_message = method_to_call(method['value'], method['name'])

					if not validation_message['valid']:
						valid = validation_message['valid']
						self.log[ method['name'] ].append(validation_message)

		return valid

	def show_error(self, name):
		errors = self.log[name]
		full_string = ''

		for error_message in errors:
			full_string += self.prefix_delimiter + error_message['message'] + self.suffix_delimiter

		return full_string

	def set_suffix_delimiter(self, suffix):
		self.suffix_delimiter = suffix

	def set_prefix_delimiter(self, prefix):
		self.prefix_delimiter = prefix


	def __init__(self):
		self.rules = []
		self.prefix_delimiter = '<p>'
		self.suffix_delimiter = '.</p>'


class ValidationMethods:

	@staticmethod
	def required(value, name):
		fail_message = name + ' is a required field'
		output = {}

		if value != '' and value != None:
			output['valid'] = True
			output['message'] = ''
		else:
			output['valid'] = False
			output['message'] = fail_message

		return output

	@staticmethod
	def letters_only(value, name):
		fail_message = name + ' contains numbers'
		output = {}

		match = re.search(r'\d', value)
		if not match:
			output['valid'] = True
			output['message'] = ''
		else:
			output['valid'] = False
			output['message'] = fail_message

		return output

	@staticmethod
	def email(value, name):
		email_regex = r'^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$'
		fail_message = name + ' was not a valid email address'
		output = {}

		match = re.match(email_regex, value)
		if match:
			output['valid'] = True
			output['message'] = ''
		else:
			output['valid'] = False
			output['message'] = fail_message

		return output

	@staticmethod
	def address(value, name):
		address_regex = r'(\d+)( \w+|\w{2,4}) (\w{2,10})(\.?)'
		fail_message = name + ' was not a valid address'
		output = {}

		match = re.match(address_regex, value)

		if match:
			output['valid'] = True
			output['message'] = ''
		else:
			output['valid'] = False
			output['message'] = fail_message

		return output