<template>
    <div>
        <b-container class="main-show-card-info">
            <b-row>
                <b-col class="img-wrapper" md="12" lg="4">
                    <b-img center :src="show.pict"/>
                </b-col>
                <b-col class="img-wrapper" md="12" lg="8">
                    <h1 class="title">{{show.title}}</h1>
                    <h5 class="title">Résumé</h5>
                    <div class="overview">
                        {{show.overview}}
                    </div>
                    <div class="date-next-ep" v-if="formated_date_next_ep">
                        Prochain épisode le {{formated_date_next_ep}} <br> Episode {{show.next_episode_num}} - Saison
                        {{show.season_next_episode_num}}
                    </div>
                    <div class="date-next-ep" v-else>
                        Aucun prochain épisode en vue :(
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>
<style>
    .main-show-card-info .title {
        padding-bottom: 5px;
        margin-bottom: 5px;
        text-align: left;
        margin-top: 25px;
    }

    .main-show-card-info {
        box-shadow: 1px 1px 4px gray;
        margin: auto;
        margin-top: 10px;
    }

    .main-show-card-info img {
        margin: 25px;
        height: 350px;
        box-shadow: 1px 1px 4px gray;
    }

    .main-show-card-info .overview {
        text-align: justify;
        padding-left: 10px;
        padding-right: 20px;
    }

    .main-show-card-info .img-wrapper {
        text-align: center;
    }

    .main-show-card-info .date-next-ep {
        background-color: #333;
        border-radius: 2px;
        color: white;
        padding: 5px;
        text-align: center;
        margin: 20px;
     }
</style>

<script>

    export default {
        name: 'Show',



        data() {
            return {

            }
        },
        props: {
            id: Number,
            formated_date_next_ep: String,
            show: Object,
        },

    }
</script>
