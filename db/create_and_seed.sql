CREATE TABLE IF NOT EXISTS `show` (
    pict VARCHAR(1024),
    last_maj DATETIME CURRENT_TIMESTAMP,
    title VARCHAR(255),
    season_next_episode_num INT,
    next_episode_date DATETIME,
    next_episode_num INT,
    api_id INT,
    id INTEGER PRIMARY KEY
);
-- populate show
INSERT INTO show (id,pict, title, season_next_episode_num, next_episode_date, next_episode_num, api_id) VALUES 
(1,'https://image.tmdb.org/t/p/w370_and_h556_bestv2/gwPSoYUHAKmdyVywgLpKKA4BjRr.jpg', 'Game of Thrones', 8, 1, '2019-04-14 14:00:00',1399),
(2,'https://image.tmdb.org/t/p/w1280/zQsEi6096L7PvowV39dtdqdW16f.jpg','Twin Peaks', NULL, NULL, NULL, 452522);


-- create notification table
CREATE TABLE IF NOT EXISTS notification (
    id_user INT,
    id_show INT,
    seen_flag BOOLEAN,
    id INTEGER PRIMARY KEY
);
-- populate notification
INSERT INTO notification (id, id_user, id_show, seen_flag) VALUES 
(1,1,1,FALSE),(2,1,2,FALSE),(3,2,1,FALSE),(4,3,1,FALSE);

CREATE TABLE IF NOT EXISTS user (
    surname VARCHAR(255),
    name VARCHAR(255),
    login VARCHAR(255),
    pwd VARCHAR(255),
    pict VARCHAR(1024),
    id INTEGER PRIMARY KEY
);
-- populate user
INSERT INTO user (id, surname, name, login, pwd, pict) VALUES 
(1, 'Fley', 'Nicolas', 'stook', 'mymdp', ''),
(2, 'Guibert', 'Rachel', 'shiva', 'mymdp', ''),
(3, 'Chapuis', 'Amelie', 'amelie', 'mymdp', '');
