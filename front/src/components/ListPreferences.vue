<template>
    <b-row>
            <b-card-group  deck class="col-4" v-for="(show,index) in list_preferences" :key="index">
                <show-card-minimal :title="show.title"
                                   :overview="show.overview"
                                   :pict="show.pict"
                                   :date_next_ep="show.date_next_ep"
                                   :show_id="show.api_id"
                                   :state="show.state"
                ></show-card-minimal>
            </b-card-group>
    </b-row>

</template>

<script>
    import ShowCardMinimal from "../components/ShowCardMinimal.vue";

    export default {
        name: "ListPreferences",
        components: {ShowCardMinimal},
        props: {
            list_preferences: {type: Array},
        }

    }

</script>

<style scoped>

</style>