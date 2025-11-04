# """A script to demonstarte the logging module"""
# import logging

# logging.basicConfig(level=logging.DEBUG, filemode='w', filename='tutorial.log', format='%(module)s - %(levelname)s - %(asctime)s - %(message)s')
# logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
# logging.info("This is a info message") # General information about the progress or state of the program
# logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
# logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
# logging.critical("This is a critical message") # A critical error that may cause the program to terminate or result in system instability


"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_file_handler = logging.FileHandler('custom_logging.log')
custom_file_handler.setLevel(logging.INFO)

custom_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
custom_file_handler.setFormatter(custom_file_formatter)

logger.addHandler(custom_file_handler)

logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message") 