# Pandas Query

Provides an efficient simple class to query a Pandas DataFrame or Series. 

## Installation

For using the package inside your projects simply install the package using `pip`:

```bash
pip install pandasquery
```

Alternatively, for development after cloning the repository use: 

```bash
pip install -e .
```

## Usage

You can instantiate queries with `Query` class and apply them memory-efficiently to the same dataframe as  you please: 

```python
from pandasquery import Query

# load the data
dataframe = load_dataframe()

# create the specific query
youth_query = Query().where("age", "<=", 30)

# apply it directly to the dataframe  
print(youth_query.apply(dataframe))
```
