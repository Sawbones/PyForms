# Pyforms! #
I created this because I noticed Tornado was lacking form validation classes, I'm mainly writing this as a way to improve my knowledge of regular expression but I figured this would help out the community as well

##API##

Getting Started:

    pyform = PyForms()
    
    pyforms.add_rule('555 Main St.', 'Address', ('required', 'address'))
    
    if pyforms.run():
        print('Everything seems valid!')
    else:
        print(pyforms.show_errors('Address'))
        
#####Current validation rules:#####

---------------------------------------

    'required'
If a field is empty it will display False

---------------------------------------

    'email'
Requires that an email is valid

---------------------------------------

    'address'
Standard US Address are currently the only thing supported, so 17th St. or 555 Moreover Stuff Ave. are both valid addresses

---------------------------------------

    'letters_only'
If numbers or special characters are found it will return False
