# Tournament Project

Tournament is the project which is a part of Introduction to Programing Nanodegree(Choose Your Path - Back-End Developer), Udacity.

## What does project do?

This project has two parts:
  First is defining the database schema using PostgreSQL database.
  The second is a Python code which can track of players and matches in tournament, using Swiss Pairing system.

## How to test run?
 1. start the virtual machine by typing `vagrant up`.
 2. log into the VM using the following command `vagrant ssh`.
 3. import the database schema using `psql` application:
    - `psql`
    - `\i tournament.sql`
    - `\q`
 4. execute the tests module by invoking the python script: `python tournament_test.py`
 5. enjoy! :)

## Contributor

Topp (Pongsakorn Tikapichart)
