CREATE TABLE IF NOT EXISTS `show` (
    pict VARCHAR(1024),
    last_maj DATETIME DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    season_next_episode_num INT,
    next_episode_date DATETIME,
    next_episode_num INT,
    api_id INT,
    id INTEGER PRIMARY KEY
);
-- populate show
INSERT INTO show (id, pict, title, season_next_episode_num, next_episode_num, next_episode_date, api_id) VALUES 
(1,'/gwPSoYUHAKmdyVywgLpKKA4BjRr.jpg', 'Game of Thrones', 8, 1, '2019-04-14 14:00:00',1402),
(2,'/zQsEi6096L7PvowV39dtdqdW16f.jpg','Twin Peaks', NULL, NULL, NULL, 1920);


-- create preference table
CREATE TABLE IF NOT EXISTS preference (
    id_user INT,
    id_show INT,
    seen_flag INT,
    id INTEGER PRIMARY KEY
);
-- populate preference
INSERT INTO preference (id, id_user, id_show, seen_flag) VALUES 
(1,1,1920,0),(2,1,1402,0),(3,2,1402,0),(4,3,1920,0);

CREATE TABLE IF NOT EXISTS user (
    surname VARCHAR(255),
    firstname VARCHAR(255),
    login VARCHAR(255),
    pwd VARCHAR(255),
    poster VARCHAR(1024),
    id INTEGER PRIMARY KEY
);
-- populate user
INSERT INTO user (id, surname, firstname, login, pwd, poster) VALUES 
(1, 'Fley', 'Nicolas', 'stook', 'mymdp', ''),
(2, 'Guibert', 'Rachel', 'shiva', 'mymdp', ''),
(3, 'Chapuis', 'Amelie', 'amelie', 'mymdp', '');
