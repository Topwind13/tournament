#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


# def connect():
#     """Connect to the PostgreSQL database.  Returns a database connection."""
#     return psycopg2.connect("dbname=tournament")

def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "TRUNCATE matches"
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = "DELETE FROM players"
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    quary = "SELECT count(*) FROM players"
    cursor.execute(quary)
    count = cursor.fetchone()
    db.commit()
    db.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    quary = "INSERT INTO players(player_name) VALUES (%s)"
    params = (name,)
    cursor.execute(quary, params)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    quary = "SELECT * from score"
    cursor.execute(quary)
    list_players_score = list(cursor.fetchall())
    db.commit()
    db.close()
    return list_players_score


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    quary = "INSERT INTO matches (winner_player_id, loser_player_id) \
    VALUES (%s, %s)"
    params = (winner, loser,)
    cursor.execute(quary, params)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    list_players = playerStandings()
    list_pair = []
    for i in range(0, len(list_players), 2):
        list_pair.append((list_players[i][0], list_players[i][1],
        list_players[i+1][0], list_players[i+1][1]))
    return list_pair
