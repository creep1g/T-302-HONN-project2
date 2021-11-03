CREATE TABLE public.ORDER(
    id SERIAL NOT NULL,
    product_id INT NOT NULL,
    merchant_id INT NOT NULL,
    buyer_id INT NOT NULL,
    card_number VARCHAR(20) NOT NULL,
    discount FLOAT4 NOT NULL,
	totalPrice FLOAT4 NOT NULL
)
TABLESPACE pg_default;

ALTER TABLE public.ORDER
    OWNER TO postgres;

/* INSERT INTO public.ORDER( */
/*     product_id, */
/*     merchant_id, */
/*     buyer_id, */
/*     card_id, */
/*     discount */
/* ) */
/* values( */
/*     1, */
/*     1, */
/*     1, */
/*     1, */
/*     1 */
/* ) */
