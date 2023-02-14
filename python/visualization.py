import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
 
engine = create_engine("postgresql:///?User=postgres&;Password=postgres&Database=esakor&Server=127.0.0.1&Port=5432")
df = pandas.read_sql("SELECT adescr, count(cthram) FROM vthramdistrictwise", engine)
print(df)
df.plot(kind="bar", x="District", y="Total Thrams")
plt.show()
