-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE players (  player_id SERIAL primary key,
                        player_name TEXT);

CREATE TABLE matches (  match_id SERIAL,
                        winner_player_id INT references players(player_id),
                        loser_player_id  INT references players(player_id));



CREATE VIEW wins AS SELECT players.player_id, players.player_name,
          count(matches.winner_player_id) As wins
FROM players left join matches
on players.player_id = matches.winner_player_id
GROUP BY players.player_id
ORDER BY wins DESC, players.player_id;


CREATE VIEW loses AS SELECT players.player_id, players.player_name,
          count(matches.loser_player_id) As loses
FROM players left join matches
on players.player_id = matches.loser_player_id
GROUP BY players.player_id
ORDER BY loses DESC, players.player_id;


CREATE VIEW score AS SELECT wins.player_id as id, wins.player_name as name, wins, (wins.wins+loses.loses) as matches
from wins left join loses
on wins.player_id = loses.player_id
ORDER BY wins DESC;
