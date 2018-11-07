<template>
    <div>
        <b-container>
            <b-row>
                <b-col cols="3">
                    <show-card-minimal :title="show.title"
                                       :overview="show.overview"
                                       :pict="show.pict"
                                       :date_next_ep="show.date_next_episode"
                                       :show_id="show.api_id"
                                       :state=0></show-card-minimal>
                </b-col>
            </b-row>
        </b-container>
        <landing-page :list_preference="list_preferences" @changestatus="changestatus"></landing-page>
    </div>

</template>
<script>

    import LandingPage from "./views/LandingPage.vue";
    import ChangePreferenceStatus from "./components/ChangePreferenceStatus.vue";
    import api from "./helpers/api.js"
    import ShowCardMinimal from "./components/ShowCardMinimal.vue";

    export default {
        name: 'App',
        components: {
            ShowCardMinimal,
            ChangePreferenceStatus,
            LandingPage,
        },
        mounted() {
            this.init()
        },
        data() {
            return {
                list_preferences: [],
                show: null,

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

                api.get("show/1399")
                    .then((res) => {
                        this.show = res;
                    }).catch((err) => console.log(err))


            },
            changestatus(event) {
                /*if (variable[1] === 0) {
                    var index = this.list_preference.findIndex(obj => {
                        return obj.show_id === variable[0]
                    });

                    this.list_preference.splice(index, 1);
                }
                else if (variable[1] === 1) {
                    this.list_preference.push()
                }*/
                this.init();

            }
        },


    }


</script>