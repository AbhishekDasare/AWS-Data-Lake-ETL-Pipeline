CREATE TABLE sales_data (
    order_id INT,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    price INT,
    total_amount INT
);

COPY sales_data
FROM 's3://data-lake-curated/curated_sales.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftRole'
CSV
IGNOREHEADER 1;
