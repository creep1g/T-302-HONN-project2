CREATE TABLE IF NOT EXISTS public.merchants(
    id SERIAL NOT NULL,
    name VARCHAR(255),
    ssn VARCHAR(11),
    email VARCHAR(255),
    phone VARCHAR(12),
	discount BOOLEAN)

TABLESPACE pg_default;

ALTER TABLE public.merchants
    OWNER to postgres;
