<template>
    <b-container>
        <list-preferences :list_preferences="list_preferences" v-on:changestatus="changestatus"></list-preferences>
        <search-bar :list_preferences="list_preferences" v-on:changestatus="changestatus"></search-bar>
    </b-container>
</template>

<script>


    import ListPreferences from "../components/ListPreferences.vue";
    import api from "../helpers/api.js"
    import SearchBar from "../components/SearchBar.vue";
    import User from '../helpers/user.js'


    export default {
        name: "LandingPage",
        components: {SearchBar, ListPreferences},
        created() {
            this.init();
        },
        data() {
            return {
                list_preferences: [],
                user: new User()
            }
        },
        methods: {
            init() {
                if(this.user.connected()) {
                    api.get("user/" + this.user.id.toString() + "/pref")
                        .then((list_pref) => {
                            this.list_preferences = list_pref.map((pref) => {
                                return {
                                    title: pref.title,
                                    overview: pref.overview,
                                    pict: pref.pict,
                                    date_next_ep: pref.date_next_ep ? Date(pref.date_next_ep) : null,
                                    api_id: pref.api_id,
                                    state: 1,
                                }
                            });
                        })
                }
            },
            changestatus(event) {
                this.init();
            }
        },

    }
</script>

<style scoped>

</style>