## Topic - Django Signals

### Question 1: Are Django Signals Executed Synchronously or Asynchronously?

**Answer**: By default, Django signals are executed synchronously.

**Explanation**:

Synchronous Execution means that when an event (like saving a model) occurs, the corresponding signal is triggered, and the signal handler runs immediately, before the next line of code after the event continues executing. In code, the `form.save()` method triggers the `post_save` signal, which is handled by `employee_post_save_handler`.

**Code Snippet**:

```python
# app/views.py
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            logger.info("Before Saving ...")
            print(f"Signal Caller thread ID: {threading.get_ident()}")

            form.save()  # This triggers the post_save signal
            logger.info("After Saving....")
            return HttpResponse('Employee Registered  Successfully!! ')
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'register.html', {'form': form})

```

```python
# app/signals.py

def employee_post_save_handler(sender, instance, created, **kwargs):
    logger.info("Signal handler started.")
    time.sleep(4)  # Delays 4 seconds
    logger.info(f"Signal handler thread ID: {threading.get_ident()}")
    # This thread ID will match the one in the caller
```

Here, if signals were asynchronous, the "After Saving...." log would appear immediately after "Before Saving ...", without waiting for the signal handler to finish. But since the signals are synchronous, the signal handler runs to completion before the "After Saving...." message is logged.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Question 2: Do Django Signals Run in the Same Thread as the Caller?

**Answer**: Yes, Django signals run in the same thread as the caller by default.

**Explanation**:

The thread is a separate path of execution in your program. If the signal handler runs in the same thread, it means it shares the same execution path as the code that triggered the signal.
In your code, both the caller (the code in register_employee) and the signal handler (the employee_post_save_handler) run in the same thread.

**Code Snippet**:
```python
# app/signals.py

def employee_post_save_handler(sender, instance, created, **kwargs):
    logger.info("Signal handler started.")
    time.sleep(4)
    logger.info(f"Signal handler thread ID: {threading.get_ident()}")     
    # This thread ID will match the one in the caller

# app/views.py

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            logger.info("Before Saving ...")
            print(f"Signal Caller thread ID: {threading.get_ident()}")
            form.save()  
```

Both threading.get_ident() calls (in the caller and the signal handler) should print the same thread ID, proving that they run in the same thread.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?

**Answer** : Yes, by default, Django signals run in the same database transaction as the caller.

**Explanation** :

Database Transaction: A group of database operations that are executed as a single unit. If any operation in the transaction fails, all the changes are rolled back.

Since signals run in the same transaction, if an error occurs in the signal handler, the entire transaction (including the save operation that triggered the signal) will be rolled back.

**Code Snippet**:
```python
# app/signals.py

def employee_post_save_handler(sender, instance, created, **kwargs):
    try:
        with transaction.atomic():
            if created:
                logger.info(f"New employee created: {instance.first_name} {instance.last_name}")
            else:
                logger.info(f"Employee updated: {instance.first_name} {instance.last_name}")
            logger.info("Raising exception to simulate a rollback.")
            raise Exception("Simulating an error to rollback transaction")
      except Exception as e:  
            logger.error(f"Exception in signal handler: {e}")     

```

Here, the signal handler raises an exception. Since the signal is part of the same transaction, this exception will cause the transaction to roll back, meaning the employee record won't be saved to the database.



----------------------------------------------------------------------------------------------------------------------------

## Topic  - Custom Classes in Python

```python
# rectangle.py
class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Length and width must be integers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers.")
        self.length = length
        self.width = width
    def __iter__(self):
        # Returns an iterator for the Rectangle class
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(25, 10)

# Iterating over the rectangle instance
for attribute in rectangle:
    print(attribute)

```
When you create an instance of Rectangle and iterate over it, you get:

# output


{'length': 25}
{'width': 10}



  
            


            

            


