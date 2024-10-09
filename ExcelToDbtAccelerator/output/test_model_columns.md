# test_model Columns

## Users

### user_id
Unique identifier for the user

- This is a key column (unique and not null)

### username
User's display name

### email
User's email address

### created_at
Timestamp of user creation

## Orders

### order_id
Unique identifier for the order

- This is a key column (unique and not null)

### user_id
User who placed the order

### total_amount
Total amount of the order

### order_date
Date when the order was placed

## Products

### product_id
Unique identifier for the product

- This is a key column (unique and not null)

### product_name
Name of the product

### price
Price of the product

### category
Category of the product

