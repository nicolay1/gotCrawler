from src.models.Show import *
from src.db.MyDBConnection import MyDBConnection
from src.models.Preference import Preference
from src.controllers.PreferenceController import PreferenceController
from src.api_helper.ApiHelperTMDB import ApiHelperTMDB

class ShowController:
    """
        This controller manages the Show model
    """

    @classmethod
    def get_one_minimal_info(cls, api_id: int, my_db: MyDBConnection):
        """
            This method creates a show object with attributes title, pict, api_id, season_next_episode_num,
            next_episode_num, date_next_episode. If the show already exists in the database, the object is created from
            the database and, depending on the date of last update, updated from API. Il the show doesn't exist in
            database, the object is created thanks to an API request, but is not created in DB (the show will be
            created in DB when the User add a preference).
        """
        show = Show.retrieve_show_from_bdd(api_id, my_db)
        if show is not None:
            # the show is in DB
            ShowController.check_for_update(my_db, show)
        else:
            api = ApiHelperTMDB()
            show = api.get_show(api_id)
        return show

    @classmethod
    def get_one_all_info(cls, show_api_id: int, my_db: MyDBConnection):
        """
            This method returns a show with complete info : in addition to title, pict, api_id, season_next_episode_num,
            next_episode_num, date_next_episode, the show object also has season_list, number_of_episodes,
            number_of_seasons attributes.
        """
        api = ApiHelperTMDB()
        api_show = api.get_show(show_api_id)

        # if the show is in database, we retrieve the db_id and update the show
        db_show = Show.retrieve_show_from_bdd(api_show.api_id, my_db)
        if db_show is not None:
            ShowController.check_for_update(my_db, db_show)
            api_show.associate_db_id(db_show.db_id)
        return api_show

    @staticmethod
    def get_on_from_db_w_api_id(my_db: MyDBConnection, show_api_id: int):
        """
            This method retrieve show from bdd with the api_id 
        """
        db_show = Show.retrieve_show_from_bdd(show_api_id, my_db)
        # may be None if no db_show found
        return db_show

    @classmethod
    def check_for_update(cls, my_db: MyDBConnection, show: Show):
        if (datetime.now() - show.last_maj).seconds > 3600:
            # the last update is too old, we update the show in API in DB.
            updated_show = ApiHelperTMDB().get_show(show.api_id)
            cls.update_show(my_db, show, updated_show)

    @classmethod
    def list_all_seasons(cls, show: Show):
        return show.season_list

    @classmethod
    def add_show(cls, my_db: MyDBConnection, title: str, pict: str, api_id: int, season_next_episode_num: int,
                 next_episode_num: int, date_next_episode:datetime):
        show = Show.retrieve_show_from_bdd(api_id, my_db)
        if show is None:
            show = Show(title, pict, api_id, season_next_episode_num, next_episode_num, date_next_episode)
            show.create_show_in_bdd(my_db)

    @classmethod
    def update_show(cls, my_db: MyDBConnection, show_db: Show, show_api: Show):
        new_seen_flag = 1
        # we check if any changes occurred concerning next episode
        if (show_db.next_episode_num != show_api.next_episode_num
                or show_db.date_next_episode != show_api.date_next_episode):
            new_seen_flag = 0
        # update of the show
        show_db.update_show(my_db=my_db, pict=show_api.pict, season_next_episode_num=show_api.season_next_episode_num,
                            next_episode_num=show_api.next_episode_num, date_next_episode=show_api.date_next_episode,
                            season_list=show_api.season_list, number_of_episodes=show_api.number_of_episodes,
                            number_of_seasons=show_api.number_of_seasons)
        # update of each preference linked to the show
        for preference in Preference.get_preference_from_show(show_db, my_db):
            if not preference.seen_flag or not new_seen_flag:
                # if the preference is unseen or if a change concerning next episode occurred, seen_flag at False
                new_seen_flag = 0
            PreferenceController.update_preference(my_db, preference, show_db, seen_flag=new_seen_flag)
