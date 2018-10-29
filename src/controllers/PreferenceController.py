from src.models.Preference import *
from src.models.User import *
from src.models.Show import *
from src.db.MyDBConnection import MyDBConnection


class PreferenceController:
    """
        This controller manage the Preference model, create preferences when needed.
    """
    @staticmethod
    def get_one(my_db: MyDBConnection, user: User, show: Show):
        preference = Preference.retrieve_preference_from_bdd(my_db=my_db, id_user=user.id, id_show=show.db_id)
        return preference

    @staticmethod
    def add_preference(my_db: MyDBConnection, user: User, show: Show, seen_flag: int):
        preference = Preference.retrieve_preference_from_bdd(my_db=my_db, id_user=user.id, id_show=show.db_id)
        if preference is None:
            preference = Preference(id_user=user.id, id_show=show.db_id, seen_flag=seen_flag)
            preference.create_preference_in_bdd(my_db)

    @classmethod
    def update_preference(cls, my_db: MyDBConnection, preference: Preference, show: Show, seen_flag):
        preference.update_preference_in_bdd(my_db=my_db, seen_flag=seen_flag)

    @staticmethod
    def delete_preference(my_db: MyDBConnection, preference: Preference):
        preference.delete_preference_in_bdd(my_db=my_db)
