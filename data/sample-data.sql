--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP INDEX IF EXISTS public.users_username_uindex;
DROP INDEX IF EXISTS public.users_id_uindex;
DROP INDEX IF EXISTS public.statuses_id_uindex;
DROP INDEX IF EXISTS public.cards_order_uindex;
DROP INDEX IF EXISTS public.cards_id_uindex;
DROP INDEX IF EXISTS public.boards_title_uindex;
DROP INDEX IF EXISTS public.boards_id_uindex;
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS users_pk;
ALTER TABLE IF EXISTS ONLY public.statuses DROP CONSTRAINT IF EXISTS statuses_pk;
ALTER TABLE IF EXISTS ONLY public.cards DROP CONSTRAINT IF EXISTS cards_pk;
ALTER TABLE IF EXISTS ONLY public.boards DROP CONSTRAINT IF EXISTS boards_pk;
ALTER TABLE IF EXISTS public.users ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.statuses ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.cards ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.boards ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.users_id_seq;
DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.statuses_id_seq;
DROP TABLE IF EXISTS public.statuses;
DROP SEQUENCE IF EXISTS public.cards_id_seq;
DROP TABLE IF EXISTS public.cards;
DROP SEQUENCE IF EXISTS public.boards_id_seq;
DROP TABLE IF EXISTS public.boards;
DROP EXTENSION IF EXISTS plpgsql;
DROP SCHEMA IF EXISTS public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: boards; Type: TABLE; Schema: public; Owner: erika
--

CREATE TABLE public.boards (
    id integer NOT NULL,
    title character varying(255) NOT NULL
);


ALTER TABLE public.boards OWNER TO erika;

--
-- Name: boards_id_seq; Type: SEQUENCE; Schema: public; Owner: erika
--

CREATE SEQUENCE public.boards_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.boards_id_seq OWNER TO erika;

--
-- Name: boards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erika
--

ALTER SEQUENCE public.boards_id_seq OWNED BY public.boards.id;


--
-- Name: cards; Type: TABLE; Schema: public; Owner: erika
--

CREATE TABLE public.cards (
    id integer NOT NULL,
    board_id integer NOT NULL,
    title character varying(255) NOT NULL,
    status_id integer NOT NULL,
    "order" integer
);


ALTER TABLE public.cards OWNER TO erika;

--
-- Name: cards_id_seq; Type: SEQUENCE; Schema: public; Owner: erika
--

CREATE SEQUENCE public.cards_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_id_seq OWNER TO erika;

--
-- Name: cards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erika
--

ALTER SEQUENCE public.cards_id_seq OWNED BY public.cards.id;


--
-- Name: statuses; Type: TABLE; Schema: public; Owner: erika
--

CREATE TABLE public.statuses (
    id integer NOT NULL,
    title character varying(255) NOT NULL
);


ALTER TABLE public.statuses OWNER TO erika;

--
-- Name: statuses_id_seq; Type: SEQUENCE; Schema: public; Owner: erika
--

CREATE SEQUENCE public.statuses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.statuses_id_seq OWNER TO erika;

--
-- Name: statuses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erika
--

ALTER SEQUENCE public.statuses_id_seq OWNED BY public.statuses.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: erika
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.users OWNER TO erika;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: erika
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO erika;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: erika
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: boards id; Type: DEFAULT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.boards ALTER COLUMN id SET DEFAULT nextval('public.boards_id_seq'::regclass);


--
-- Name: cards id; Type: DEFAULT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.cards ALTER COLUMN id SET DEFAULT nextval('public.cards_id_seq'::regclass);


--
-- Name: statuses id; Type: DEFAULT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.statuses ALTER COLUMN id SET DEFAULT nextval('public.statuses_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: boards; Type: TABLE DATA; Schema: public; Owner: erika
--

INSERT INTO public.boards VALUES (1, 'Board1');
INSERT INTO public.boards VALUES (2, 'Board2');


--
-- Data for Name: cards; Type: TABLE DATA; Schema: public; Owner: erika
--

INSERT INTO public.cards VALUES (1, 1, 'Card1', 0, NULL);
INSERT INTO public.cards VALUES (2, 2, 'Card2', 3, NULL);
INSERT INTO public.cards VALUES (3, 1, 'Card3', 1, NULL);
INSERT INTO public.cards VALUES (4, 2, 'Card4', 2, NULL);


--
-- Data for Name: statuses; Type: TABLE DATA; Schema: public; Owner: erika
--

INSERT INTO public.statuses VALUES (0, 'new');
INSERT INTO public.statuses VALUES (1, 'in progress');
INSERT INTO public.statuses VALUES (2, 'testing');
INSERT INTO public.statuses VALUES (3, 'done');


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: erika
--



--
-- Name: boards_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erika
--

SELECT pg_catalog.setval('public.boards_id_seq', 1, false);


--
-- Name: cards_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erika
--

SELECT pg_catalog.setval('public.cards_id_seq', 1, false);


--
-- Name: statuses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erika
--

SELECT pg_catalog.setval('public.statuses_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: erika
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: boards boards_pk; Type: CONSTRAINT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.boards
    ADD CONSTRAINT boards_pk PRIMARY KEY (id);


--
-- Name: cards cards_pk; Type: CONSTRAINT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.cards
    ADD CONSTRAINT cards_pk PRIMARY KEY (id);


--
-- Name: statuses statuses_pk; Type: CONSTRAINT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.statuses
    ADD CONSTRAINT statuses_pk PRIMARY KEY (id);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: erika
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- Name: boards_id_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX boards_id_uindex ON public.boards USING btree (id);


--
-- Name: boards_title_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX boards_title_uindex ON public.boards USING btree (title);


--
-- Name: cards_id_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX cards_id_uindex ON public.cards USING btree (id);


--
-- Name: cards_order_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX cards_order_uindex ON public.cards USING btree ("order");


--
-- Name: statuses_id_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX statuses_id_uindex ON public.statuses USING btree (id);


--
-- Name: users_id_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX users_id_uindex ON public.users USING btree (id);


--
-- Name: users_username_uindex; Type: INDEX; Schema: public; Owner: erika
--

CREATE UNIQUE INDEX users_username_uindex ON public.users USING btree (username);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

