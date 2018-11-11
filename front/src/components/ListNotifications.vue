<template>
    <b-nav-item-dropdown right>        <template slot="button-content">
          <em>Notifications <b-badge variant="light">{{nombre_notif}}</b-badge></em>
        </template>
        <b-dropdown-item id="notificationslist">
            <notification v-for="(show, index) in notif_list"
                    :key="index" :show="show" :name="show.api_id" :user_id="id_user" v-on:notificationAcknowledged="init"></notification>
        </b-dropdown-item>
    </b-nav-item-dropdown>
</template>

<script>
    import Notification from "./Notification.vue";
    import api from "../helpers/api.js"

    export default {
        name: "ListNotifications",
        components: {Notification},
        props: {
            id_user: Number
        },
        data() {
            return {
                notif_list: [],
                nombre_notif:null
            }
        },
        created() {
            this.init()
        },
        methods: {
            init() {
                console.log(this.id_user)
                api.get("user/" + this.id_user + "/pref").then(
                    (res) => {
                        this.notif_list = res.filter((show) => {
                            return !show.new_ep_acknoweldged & (show.next_ep_date!=null);
                        }).map((show) => {
                            return {
                                title: show.title,
                                next_ep_num: show.next_ep_num,
                                next_season_num: show.next_season_num,
                                next_ep_date: show.next_ep_date,
                                id: show.api_id
                            }
                        });
                        this.nombre_notif=this.notif_list.length
                    }
                )
            }
        }
    }
</script>

<style scoped>

</style>