# we can import various way

# import s06_modules_packages_call_function_to_other_location
# s06_modules_packages_call_function_to_other_location.fun_in_module()


# import s06_modules_packages_call_function_to_other_location as mm
# mm.fun_in_module()

# only import function
# from s06_modules_packages_call_function_to_other_location import fun_in_module
# fun_in_module()

# this is not good practice for use but we can do this way too.add()
from s06_modules_packages_call_function_to_other_location import *
fun_in_module()
