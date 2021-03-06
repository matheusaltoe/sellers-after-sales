PGDMP     4                     y            sellerdb    12.8 (Debian 12.8-1.pgdg100+1)    12.8 (Debian 12.8-1.pgdg100+1)     |           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            }           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ~           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16384    sellerdb    DATABASE     x   CREATE DATABASE sellerdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE sellerdb;
                postgres    false            ?            1259    16399    channel    TABLE     \   CREATE TABLE public.channel (
    id integer NOT NULL,
    description character varying
);
    DROP TABLE public.channel;
       public         heap    postgres    false            ?            1259    16397    channel_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.channel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.channel_id_seq;
       public          postgres    false    205            ?           0    0    channel_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.channel_id_seq OWNED BY public.channel.id;
          public          postgres    false    204            ?            1259    16387    customer    TABLE     ?   CREATE TABLE public.customer (
    id integer NOT NULL,
    name character varying,
    email character varying,
    phone character varying
);
    DROP TABLE public.customer;
       public         heap    postgres    false            ?            1259    16385    customer_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.customer_id_seq;
       public          postgres    false    203            ?           0    0    customer_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.customer_id_seq OWNED BY public.customer.id;
          public          postgres    false    202            ?            1259    16412 	   scheduler    TABLE     ?   CREATE TABLE public.scheduler (
    id integer NOT NULL,
    date_hour timestamp without time zone,
    message character varying,
    status_send boolean,
    customer_id integer,
    channel_id integer
);
    DROP TABLE public.scheduler;
       public         heap    postgres    false            ?            1259    16410    scheduler_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.scheduler_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.scheduler_id_seq;
       public          postgres    false    207            ?           0    0    scheduler_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.scheduler_id_seq OWNED BY public.scheduler.id;
          public          postgres    false    206            ?
           2604    16402 
   channel id    DEFAULT     h   ALTER TABLE ONLY public.channel ALTER COLUMN id SET DEFAULT nextval('public.channel_id_seq'::regclass);
 9   ALTER TABLE public.channel ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            ?
           2604    16390    customer id    DEFAULT     j   ALTER TABLE ONLY public.customer ALTER COLUMN id SET DEFAULT nextval('public.customer_id_seq'::regclass);
 :   ALTER TABLE public.customer ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            ?
           2604    16415    scheduler id    DEFAULT     l   ALTER TABLE ONLY public.scheduler ALTER COLUMN id SET DEFAULT nextval('public.scheduler_id_seq'::regclass);
 ;   ALTER TABLE public.scheduler ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            w          0    16399    channel 
   TABLE DATA           2   COPY public.channel (id, description) FROM stdin;
    public          postgres    false    205            u          0    16387    customer 
   TABLE DATA           :   COPY public.customer (id, name, email, phone) FROM stdin;
    public          postgres    false    203            y          0    16412 	   scheduler 
   TABLE DATA           a   COPY public.scheduler (id, date_hour, message, status_send, customer_id, channel_id) FROM stdin;
    public          postgres    false    207            ?           0    0    channel_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.channel_id_seq', 4, true);
          public          postgres    false    204            ?           0    0    customer_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.customer_id_seq', 3, true);
          public          postgres    false    202            ?           0    0    scheduler_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.scheduler_id_seq', 7, true);
          public          postgres    false    206            ?
           2606    16409    channel channel_description_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.channel
    ADD CONSTRAINT channel_description_key UNIQUE (description);
 I   ALTER TABLE ONLY public.channel DROP CONSTRAINT channel_description_key;
       public            postgres    false    205            ?
           2606    16407    channel channel_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.channel
    ADD CONSTRAINT channel_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.channel DROP CONSTRAINT channel_pkey;
       public            postgres    false    205            ?
           2606    16395    customer customer_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    203            ?
           2606    16420    scheduler scheduler_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.scheduler
    ADD CONSTRAINT scheduler_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.scheduler DROP CONSTRAINT scheduler_pkey;
       public            postgres    false    207            ?
           1259    16396    ix_customer_email    INDEX     N   CREATE UNIQUE INDEX ix_customer_email ON public.customer USING btree (email);
 %   DROP INDEX public.ix_customer_email;
       public            postgres    false    203            ?
           2606    16426 #   scheduler scheduler_channel_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.scheduler
    ADD CONSTRAINT scheduler_channel_id_fkey FOREIGN KEY (channel_id) REFERENCES public.channel(id);
 M   ALTER TABLE ONLY public.scheduler DROP CONSTRAINT scheduler_channel_id_fkey;
       public          postgres    false    2801    207    205            ?
           2606    16421 $   scheduler scheduler_customer_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.scheduler
    ADD CONSTRAINT scheduler_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(id);
 N   ALTER TABLE ONLY public.scheduler DROP CONSTRAINT scheduler_customer_id_fkey;
       public          postgres    false    203    207    2796            w   -   x?3?,?-?2?,(-??2?,?H,)N,(?2?L?M???????? ?}
B      u   d   x?%?;
?0D???H6!?v;?`?	?|D?o?S?1[?
g+w???t?f ??(?-?a?;???;??%??c-??*??" E\}?ģѪ??"~ ??      y   ?   x???1?0??9?/P;M??9??%P#AS%???c$??????-?ej??!?d???Z???d<?e|@2??dMr`?a]????p?	?4?=NU??3??Ak???G?օ??6r?xк?8	#???1N񢖀M?k??B?????l|??`????[I?.?1?o?_c???D?     