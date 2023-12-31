PGDMP      *        	    
    {            sales_dashboard_db    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16917    sales_dashboard_db    DATABASE     �   CREATE DATABASE sales_dashboard_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
 "   DROP DATABASE sales_dashboard_db;
                postgres    false            �            1259    16919    tb_purchase    TABLE     �   CREATE TABLE public.tb_purchase (
    purchase_no smallint NOT NULL,
    model_name character varying(50) NOT NULL,
    sales_man character varying(100) NOT NULL
);
    DROP TABLE public.tb_purchase;
       public         heap    postgres    false            �            1259    16918    tb_purchase_purchase_no_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_purchase_purchase_no_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.tb_purchase_purchase_no_seq;
       public          postgres    false    216            �           0    0    tb_purchase_purchase_no_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.tb_purchase_purchase_no_seq OWNED BY public.tb_purchase.purchase_no;
          public          postgres    false    215            �            1259    16933    tb_sales_invoice    TABLE     	  CREATE TABLE public.tb_sales_invoice (
    id smallint NOT NULL,
    purchase_no smallint NOT NULL,
    invoice_date date NOT NULL,
    invoice_stat smallint NOT NULL,
    CONSTRAINT tb_sales_invoice_invoice_stat_check CHECK ((invoice_stat = ANY (ARRAY[0, 1])))
);
 $   DROP TABLE public.tb_sales_invoice;
       public         heap    postgres    false            �            1259    16932    tb_sales_invoice_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_sales_invoice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.tb_sales_invoice_id_seq;
       public          postgres    false    218            �           0    0    tb_sales_invoice_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.tb_sales_invoice_id_seq OWNED BY public.tb_sales_invoice.id;
          public          postgres    false    217            U           2604    16925    tb_purchase purchase_no    DEFAULT     �   ALTER TABLE ONLY public.tb_purchase ALTER COLUMN purchase_no SET DEFAULT nextval('public.tb_purchase_purchase_no_seq'::regclass);
 F   ALTER TABLE public.tb_purchase ALTER COLUMN purchase_no DROP DEFAULT;
       public          postgres    false    215    216    216            V           2604    16945    tb_sales_invoice id    DEFAULT     z   ALTER TABLE ONLY public.tb_sales_invoice ALTER COLUMN id SET DEFAULT nextval('public.tb_sales_invoice_id_seq'::regclass);
 B   ALTER TABLE public.tb_sales_invoice ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    16919    tb_purchase 
   TABLE DATA           I   COPY public.tb_purchase (purchase_no, model_name, sales_man) FROM stdin;
    public          postgres    false    216   �       �          0    16933    tb_sales_invoice 
   TABLE DATA           W   COPY public.tb_sales_invoice (id, purchase_no, invoice_date, invoice_stat) FROM stdin;
    public          postgres    false    218   +       �           0    0    tb_purchase_purchase_no_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.tb_purchase_purchase_no_seq', 1, false);
          public          postgres    false    215            �           0    0    tb_sales_invoice_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.tb_sales_invoice_id_seq', 1, false);
          public          postgres    false    217            Y           2606    16927    tb_purchase tb_purchase_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.tb_purchase
    ADD CONSTRAINT tb_purchase_pkey PRIMARY KEY (purchase_no);
 F   ALTER TABLE ONLY public.tb_purchase DROP CONSTRAINT tb_purchase_pkey;
       public            postgres    false    216            [           2606    16947 &   tb_sales_invoice tb_sales_invoice_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.tb_sales_invoice
    ADD CONSTRAINT tb_sales_invoice_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.tb_sales_invoice DROP CONSTRAINT tb_sales_invoice_pkey;
       public            postgres    false    218            \           2606    16940 2   tb_sales_invoice tb_sales_invoice_purchase_no_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_sales_invoice
    ADD CONSTRAINT tb_sales_invoice_purchase_no_fkey FOREIGN KEY (purchase_no) REFERENCES public.tb_purchase(purchase_no);
 \   ALTER TABLE ONLY public.tb_sales_invoice DROP CONSTRAINT tb_sales_invoice_purchase_no_fkey;
       public          postgres    false    216    218    4697            �   %  x�}T�N�0<�_�/@��#��"p �����%*H����"�H���k_���ٙ٘Vl}�ۿ��p���9�i
��*�����xnv��9J�����e��}��ޛ���r���`I��Hl���xz���7�+
j!6�'pH��	R�6�S>r#�+G��F�n�I9+Kvɻ�M�8�b�!������+�����+��ч6ؚ5h
&�&��A��|z���5���.�����g�,9�b�A�|���|b �Y�U��H:�A�!o���Yr���+x����`�n��ߵ��      �   ]  x�E�ɍ�0��\��3��?�a��W�0���!01ob���D�L�6�^���-�%Ҧ�h".�4]Dq���tu�%�M�#.�jډq�fS'R�%�A$�_������� ��}7
�}���(��	�w���|܍B{��~7
���~7
���v7
�]�z7
�]�r7
�-���贷P�w���B}ݍF{��{G�[���;��B��7n4�[�{�����VH��>�0M��F�B;�a���r�.4���
�,�a�B=�a��g9��c�[�(�����0^{}[�=��B��0)$Y��I�R龱�faX���,0���Q`d/{�^��x��,K	�����=���*��     