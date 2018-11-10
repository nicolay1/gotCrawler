<template>
    <div class="card season-card">
        <div class="container card-header">
            <div class="row season-card-header">
                <div class="col-lg-2 col-md-6">
                    <img :src="poster">
                </div>
                <div class="col-lg-2 col-md-6 num_season">
                    Saison n°{{num_season}}
                </div>
                <div class="col-lg-7 col-md-6 name">
                    {{name}}
                </div>
                <div class="expand-icon toggle-button" v-b-toggle.num_season>
                    <span class="expand-icon-text d-none d-sm-inline ">Voir plus</span>
                    <font-awesome-icon icon="angle-down" size="1x"/>
                </div>
            </div>
        </div>
        <b-collapse visible id="num_season">
            <div class="card-body">
                <p>{{overview}}</p>
                <div class="separator"></div>
                <div>
                    <span class="toggle-button" v-b-toggle.episodesList>Épisodes <font-awesome-icon icon="angle-down"
                                                                                                   size="1x"/></span>
                </div>
                <b-collapse class="episodes-collapse " id="episodesList">
                    <Episode
                            v-for="(episode, index) in episode_list"
                            :key="index"
                            :ep_number="episode.num_ep"
                            :title="episode.name"
                            :overview="episode.summary"
                            :authors="episode.list_author"
                            :actors="episode.list_actor"
                    ></Episode>
                </b-collapse>
            </div>
        </b-collapse>
    </div>

</template>

<script>
    import Episode from "./Episode.vue";
    import api from "../helpers/api.js";


    export default {
        name: "season",
        components: {
            Episode
        },
        mounted() {
            this.init()
        },
        data() {
            return {
                episode_list: Array,
                name: String,
                overview: String,
                poster: String,
            }
        },
        props: {
            id_show: Number,
            num_season: Number,

        },
        methods: {
            init() {
                api.get("show/" + this.id_show + "/season/" + this.num_season)
                    .then((res) => {
                        this.episode_list = res.list_episodes;
                        this.name = res.name;
                        this.overview = res.overview;
                        this.poster = res.poster;
                    })
                    .catch((err) => console.log(err));
            }
        }, watch: {
            num_season: function () {
                this.init()
            },

        }
    }
</script>

<style scoped>

    .season-card-header {
        text-align: center;
        position: relative;
    }

    .season-card .expand-icon {
        position: absolute;
        bottom: calc(-1.25rem + 2px);
        right: calc(-.75rem + 2px);
    }

    .season-card .expand-icon-text {
        position: relative;
        margin-right: 5px;
    }

    .season-card img {
        max-height: 100px;
    }

    .season-card .separator{
        width: 100%;
        padding: 0;
        margin: 10px 0px;
        border-top: 1px solid rgba(0,0,0,.125);
        height: 0;
        margin-bottom: 15px;
    }

    .season-card .toggle-button {
        background-color: #eee;
        cursor: pointer;
        padding: 5px;
        margin: 5px;
    }

    .season-card .episodes-collapse{
        margin-top:10px;
    }
</style>