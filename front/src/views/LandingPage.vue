<template>
    <b-container>
        <season :id_show=1399 :num_season=2></season>
        <b-row>
            <b-col cols="3" v-for="(show,index) in list_preference" :key="index">
                <show-card-minimal :title="show.title"
                           :overview="show.overview"
                           :pict="show.pict"
                           :date_next_ep="show.date_next_ep"
                           :show_id="show.api_id"
                           :state="show.state"
                ></show-card-minimal>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import ShowCardMinimal from "../components/ShowCardMinimal.vue";
    import Season from "../components/Season.vue";

    export default {
        name: "LandingPage",
        components: {Season, ShowCardMinimal},
        data(){
            return{
            }
        },
        props: {
            list_preference: {type: Array},
        }
    }
</script>

<style scoped>

</style>