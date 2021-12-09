# This is code to pull data from a CSV file and load it onto a WAMP server
# Rick Sturza Rlsturza@student.rtc.edu
# Partner - Josh Furukawa joshfurukawa@gmail.com
# Partner - Sarmad Jubba sarmadkubba@gmail.com
# SQL CNE 340
# Base code furnished by Justin Ellis jellis@rtc.edu
# Reference https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# Reference https://www.w3schools.com/sql/sql_ref_drop_index.asp
import pandas
from sqlalchemy import create_engine

hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "cne340"


engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))


tables = pandas.read_csv(r"C:\Users\joshf\PycharmProjects\SeahawksDB\touchdown.csv",
                         header='infer', index_col='Rk', usecols=None, squeeze=False, mangle_dupe_cols=True, dtype=None,
                         engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False,
                         skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True,
                         verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
                         keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False,
                         chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None,
                         quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None,
                         encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None,
                         on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False,
                         float_precision=None, storage_options=None)

connection = engine.connect()
tables.to_sql('hawkdown', con=engine, if_exists='append')


engine.execute('CREATE TABLE Hawk_Down Like hawkdown')
engine.execute('INSERT INTO Hawk_Down SELECT DISTINCT (Rk), Date, Opp, Result, Quarter, Dist, Type, Detail FROM hawkdown ')
engine.execute('DROP TABLE hawkdown')
engine.execute('ALTER TABLE Hawk_Down DROP COLUMN Date')
engine.execute('ALTER TABLE Hawk_Down RENAME TO hawk_touchdowns')
connection.close()

# ^ Close extension to database
