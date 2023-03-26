#!/bin/sh

DATABASE_URL='postgresql+psycopg2://celeste_and_peter:testpw@localhost/celeste_and_peter' gunicorn app:app
