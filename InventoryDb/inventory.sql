CREATE TABLE IF NOT EXISTS public.inventory(
    id SERIAL NOT NULL,
    merchantId INT,
    productName VARCHAR(255),
    price FLOAT,
    quantity INT,
	reserved INT
    )

TABLESPACE pg_default;

ALTER TABLE public.inventory
    OWNER to postgres;
