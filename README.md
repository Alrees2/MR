# MR

MR is a Python library that stops code execution based on a specified timeout and deletes a log entry after the timeout expires.

## Installation

You can install MR via pip:

```sh
pip install MR
```

## Usage

Here is an example of how to use the MR library:

```python
from MR import run_with_timeout

@run_with_timeout(timeout=10, unit='seconds')
def my_function():
    # Your code here
    print("Function is running")

try:
    my_function()
except TimeoutError as e:
    print(e)
```

In this example, the `my_function` will stop executing if it takes more than 10 seconds to complete. The `TimeoutError` exception will be raised if the execution time exceeds the specified timeout.

## Functions

### `run_with_timeout(timeout, unit='seconds')`
- `timeout`: The timeout duration.
- `unit`: The unit of time for the timeout ('seconds', 'minutes', 'hours', 'days').

This decorator stops the code execution and deletes the log entry after the timeout expires.
