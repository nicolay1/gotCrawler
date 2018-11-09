<template>
    <div id="app">
        <notifications 
                    position="top right"
                    :speed="500"
                    :duration="10000"/>
        <b-container v-if="show">
        <router-view :list_preference="list_preferences">

        </router-view>

    </div>
</template>

<script>
    import api from "./helpers/api.js"

    export default {
        name: 'App',
        mounted() {
            this.init();
        },
        data() {
            return {
                list_preferences: [],
            }
        },
        methods: {
            init() {
                api.get("user/3/pref")
                    .then((list_pref) => {
                        this.list_preferences = list_pref.map((pref) => {
                            return {
                                title: pref.title,
                                overview: pref.overview,
                                pict: pref.pict,
                                date_next_ep: pref.date_next_ep ? Date(pref.date_next_ep) : null,
                                show_id: pref.api_id,
                                state: 1,
                            }
                        });
                    })
            },
            changestatus(event) {
                this.init();
            }
        },

    }
</script>

<style>
    #app {

    }
</style>