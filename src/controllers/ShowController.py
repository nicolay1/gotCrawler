from src.models.Show import *
from db.MyDBConnection import MyDBConnection

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
            if (datetime.now()-show.last_maj).seconds > 3600:
                # the last update is too old, we update the show in API in DB.
                #TODO call API
                cls.update_show(my_db, show, pict, season_next_episode_num, next_episode_num, date_next_episode)
        else:
            #TODO call API
            show = Show(title, pict, api_id, season_next_episode_num, next_episode_num, date_next_episode)
        return show

    @classmethod
    def get_one_all_info(cls, show_api_id: int, my_db: MyDBConnection):
        """
            This method returns a show with complete info : in addition to title, pict, api_id, season_next_episode_num,
            next_episode_num, date_next_episode, the show object also has season_list, number_of_episodes,
            number_of_seasons attributes.
        """
        show = cls.get_one_minimal_info(show_api_id, my_db)
        #TODO call API
        cls.update_show(my_db=my_db, show=show, season_list=season_list, number_of_episodes=number_of_episodes,
                        number_of_seasons=number_of_seasons)
        return show


    @classmethod
    def list_all_seasons(cls, show: Show):
        return show.season_list

    @classmethod
    def add_show(cls, my_db:MyDBConnection, title: str, pict: str, api_id: int, season_next_episode_num: int,
                 next_episode_num: int, date_next_episode:datetime):
        show = Show(title, pict, api_id, season_next_episode_num, next_episode_num, date_next_episode)
        show.create_show_in_bdd(my_db)

    @classmethod
    def update_show(cls, my_db: MyDBConnection, show: Show, pict: str = None, season_next_episode_num: int = None,
                    next_episode_num: int = None, date_next_episode: datetime = None, season_list: List[Season] = None,
                    number_of_episodes: int = None, number_of_seasons: int = None):
        show.update_show(my_db=my_db, pict=pict, season_next_episode_num=season_next_episode_num,
                         next_episode_num=next_episode_num, date_next_episode=date_next_episode,
                         season_list=season_list, number_of_episodes=number_of_episodes,
                         number_of_seasons=number_of_seasons)
