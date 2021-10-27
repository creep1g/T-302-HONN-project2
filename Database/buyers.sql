CREATE TABLE IF NOT EXISTS public.buyers(
    id SERIAL NOT NULL,
    name VARCHAR(255),
    ssn VARCHAR(8),
    email VARCHAR(255),
    phone VARCHAR(12)
)

TABLESPACE pg_default;

ALTER TABLE public.buyers
    OWNER to postgres;
