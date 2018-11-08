<template>
    <div id="app">
        <router-view :list_preference="list_preferences">

        </router-view>
    </div>
</template>

<script>
    import api from "./helpers/api.js"


    export default {
        name: 'App',
        mounted() {
            this.init()
        },
        data() {
            return {
                list_preferences: [],

            }

        },
        methods: {
            init() {
                api.get("user/3/pref")
                    .then((res) => {
                        this.list_preferences = res;
                        for (let i = 0; i < this.list_preferences.length; i++) {
                            this.list_preferences[i].state = 1;
                        }
                    }).catch((err) => console.log(err));


            },
            changestatus() {

                this.init();

            }
        },

    }
</script>

<style>
    #app {

    }
</style>