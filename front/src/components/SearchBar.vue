<template>
    <b-container class="search_bar">
        <b-row class="justify-content-md-center">
            <b-col cols="6" align="Center">
                <div class="input-group mb-3">
                    <input v-model="show_searched"
                           v-on:keyup.enter="show_results(show_searched)"
                           v-on:click="clean_message"
                           type="text"
                           class="form-control"
                           aria-label="Serie's name"
                           aria-describedby="button-addon2">
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" id="button-addon2"
                                v-on:click="show_results(show_searched)">Recherche
                        </button>
                    </div>
                </div>
            </b-col>
        </b-row>
        <div class="row ">
            <b-card-group  deck class="col-4" v-for="(show,index) in show_list" :key="index">

                <show-card-minimal class="showcard_class"
                                   :title="show.title"
                                   :overview="show.overview"
                                   :pict="show.pict"
                                   :date_next_ep="show.date_next_episode"
                                   :show_id="show.api_id"
                                   :state="show.state"
                >
                </show-card-minimal>
            </b-card-group>


        </div>
    </b-container>
</template>

<script>
    import Episode from "./Episode.vue";
    import ShowCardMinimal from "./ShowCardMinimal.vue";
    import api from '../helpers/api.js';

    export default {
        name: "SearchBar",
        components: {
            Episode,
            ShowCardMinimal
        },
        props: {
            list_preferences: {type: Array}
        },
        computed: {
            listPreferencesId() {
                return this.list_preferences.map((pref) => {
                    return pref.api_id;
                })
            }
        },
        created(){
            api.get('show/trending').then((res)=>{
                this.show_list=this.merge_pref_with_search_results(res)
            })
        },
        data() {
            return {
                show_searched: "Game of Thrones...",
                show_list: Array

            }
        },
        methods: {
            merge_pref_with_search_results: function (show_list) {
                return show_list.map((show) => {
                    show.state = this.listPreferencesId.includes(show.api_id) ? 1 : 0;
                    return show
                })
            },
            show_results: function (show_searched) {
                api
                    .get('show/search', {q: show_searched})
                    .then((response) => {
                        this.show_list = this.merge_pref_with_search_results(response)
                    })
            },
            clean_message: function () {
                this.show_searched = ""
            }
        }
    }
</script>

<style scoped>
    .search_bar {
        padding: 2px 2px 2px 2px;
        margin: 30px;
    }

    .showcard_class {
        margin: 5px 5px 5px 5px;
    }
</style>