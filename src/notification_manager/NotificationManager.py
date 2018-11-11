from threading import Thread
import datetime
import time
import random

from src.db.MyDBConnection import MyDBConnection

from src.controllers.ShowController import ShowController

from src.config import CONFIG

class NotificationManager(Thread):

    notif_step = 3600  # check for update every hours
    max_request_per_minute = 30
    absolute_max_request_per_second = 100
    min_time_between_maj = 10  # in s

    def __init__(self):
        """
            This class Manage the notifications updates. It's running in background, checking regulary if some notifications
            have to be updated.
        """
        Thread.__init__(self)
        self.name = random.random()
        self.notif_step = 3600  # check for update every hours
        self.max_request_per_minute = 3
        self.absolute_max_request_per_second = 100
        self.min_time_between_maj = 10  # in s
        self.__sleep_between_request = max(60/self.max_request_per_minute, 1/self.absolute_max_request_per_second)
        self.my_db = MyDBConnection(CONFIG["db_path"])

    def run(self):
        while True:
            # retrieve all shows which have been chosen by a user
            all_shows_with_a_pref = ShowController.get_all_with_a_pref(self.my_db)
            print(list(map(lambda x:x.title, all_shows_with_a_pref)))

            # calculate the 'at least' number of shows we need to update
            nb_min_show_to_update = len(all_shows_with_a_pref)

            # for each show, we check for update
            for show in all_shows_with_a_pref:
                #print("check for updating : ", show.title)

                # if the time since last maj is too low, we skip it
                time_since_last_maj = (datetime.datetime.now() - show.last_maj).total_seconds()
                if time_since_last_maj > self.min_time_between_maj:
                    # the update
                    ShowController.check_for_update(self.my_db, show)

                # we sleep according to the time we have to send all the request and the number of request we have to update.
                # it's the max between the number of second to wait to spread the request and the min sleep we need to not
                # being stopped by the api
                time_to_sleep = max(
                    self.min_time_between_maj/nb_min_show_to_update, self.__sleep_between_request
                )
                time.sleep(time_to_sleep)