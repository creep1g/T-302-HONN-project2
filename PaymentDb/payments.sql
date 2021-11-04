CREATE TABLE public.PAYMENTS(
    id SERIAL NOT NULL,
    order_id INT NOT NULL,
    result BOOLEAN NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE public.PAYMENTS
    OWNER TO postgres;
