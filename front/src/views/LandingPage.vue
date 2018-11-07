<template>
    <b-container>
        <b-row>
            <b-col cols="3" v-for="show in list_preference">
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

    export default {
        name: "LandingPage",
        components: {ShowCardMinimal},
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