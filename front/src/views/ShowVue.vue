<template>
    <b-container>
        <b-row>
            <b-col cols="12">
                <Show :id="id"
                      :formated_date_next_ep="formated_date_next_ep"
                      :show="show"
                ></Show>
            </b-col>
        </b-row>

        <b-row>
            <b-col cols="12">
                <b-dropdown id="dropdown"
                            name="dropdown"
                            v-model="ddTestVm.ddTestSelectedOption"
                            text="Numéro de Saison"
                            variant="secondary"
                            class="m-md-2">
                    <b-dropdown-item disabled value="0">Sélectionner un n° de Saison</b-dropdown-item>
                    <b-dropdown-item v-for="(season, index) in season_list"
                                     :key="index"
                                     :value="season.num_season"
                                     @click="ddTestVm.ddTestSelectedOption = season.num_season">
                        {{season.num_season}}

                    </b-dropdown-item>
                </b-dropdown>

                <Season
                        :id_show="id"
                        :num_season="ddTestVm.ddTestSelectedOption"></Season>
            </b-col>
        </b-row>

    </b-container>
</template>


<script>
    import Show from "../components/Show.vue";
    import api from "../helpers/api";
    import Season from "../components/Season.vue";

    export default {
        name: "ShowVue",
        components: {Season, Show},
        data() {
            return {

                ddTestVm: {
                    originalValue: [],
                    ddTestSelectedOption: 1,
                    disabled: false,
                    readonly: false,
                    visible: true,

                },
                season_list: [],
                formated_date_next_ep: new Date().toLocaleDateString(),
                show: {},
            }
        },
        created() {
            this.init()
        },
        props: {
            id: Number,
        },

        methods: {
            init() {
                api.get('show/' + this.id)
                    .then((res) => {
                        this.show = res;
                        this.formated_date_next_ep = new Date(res.date_next_episode).toLocaleDateString() ? new Date(res.date_next_episode).toLocaleDateString() : null;
                        this.season_list = res.season_list;
                    })
                    .catch((err) => console.log(err));
            }
        }
    }
</script>

<style scoped>

</style>