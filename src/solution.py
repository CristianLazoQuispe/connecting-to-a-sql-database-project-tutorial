# importing the reusable functions
# We created the "connect" function on the file reusable_functions.py
# and we are going to use it every time we want to connect to the database
# Hola
import matplotlib.pyplot as plt 
from reusable_functions import connect, run_file, run_query
# importing pandas
import pandas as pd

# 1) Connect to the database here using the SQLAlchemy's create_engine function
# connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
# engine = create_engine(connection_string)
# engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
# engine.execute("""
# CREATE TABLE publishers(
#     publisher_id INT NOT NULL,
#     name VARCHAR(255) NOT NULL,
#     PRIMARY KEY(publisher_id)
# );
# """)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
# engine.execute("INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');")


# 4) Use pandas to print one of the tables as dataframes using read_sql function
# result_dataFrame = pd.read_sql("Select * from books;", engine)
# print(result_dataFrame)
