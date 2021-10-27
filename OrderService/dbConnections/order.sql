CREATE TABLE public.ORDER(
    id SERIAL NOT NULL,
    product_id INT NOT NULL,
    merchant_id INT NOT NULL,
    buyer_id INT NOT NULL,
    card_id INT NOT NULL,
    discount FLOAT4 NOT NULL
)
TABLESPACE pg_default;

ALTER TABLE public.ORDER
    OWNER TO postgres;

CREATE TABLE public.CreditCard(
    id SERIAL NOT NULL,
    cardNumber VARCHAR(255) NOT NULL,
    expirationMonth INT NOT NULL,
    expirationDay INT NOT NULL,
    cvc INT NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE public.CreditCard
    OWNER TO postgres;


INSERT INTO public.ORDER(
    product_id,
    merchant_id,
    buyer_id,
    card_id,
    discount
)
values(
    1,
    1,
    1,
    1,
    1
)