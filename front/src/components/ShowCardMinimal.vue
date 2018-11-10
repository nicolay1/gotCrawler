<template>
    <b-card
    >
        <b-card-img :src="pict"
                    top
                    v-on:click="goToShow"
                    height=400></b-card-img>

        <div class="card-title show_title">
            <b-row>
                <b-col cols="8">
                    {{title}}
                </b-col>

                <b-col cols="1">
                <span class="btn_pref">
                    <change-preference-status :show_id="show_id" :state="data_state"
                    ></change-preference-status>

                </span>
                </b-col>
            </b-row>
        </div>
        <b-card-body class="card-text col-12">
        </b-card-body>

        <b-card-footer v-if="date_next_ep">Prochain épisode : {{date_next_ep}}</b-card-footer>

    </b-card>

</template>

<script>

    import ChangePreferenceStatus from "./ChangePreferenceStatus.vue";

    export default {
        name: 'ShowCardMinimal',
        components: {ChangePreferenceStatus},
        props: {
            title: String,
            overview: String,
            pict: String,
            date_next_ep: Date,
            show_id: Number,
            state: Number

        },
        data() {
            //Ligne commentée car tant que la date n'est pas géré dans les préférences ça fait tout bugué
            //let date_to_string = this.date_next_ep.toLocaleDateString();
            return {
                data_state: this.state,
                //date_to_string: date_to_string,
            }
        },
        methods: {
            goToShow() {
                this.$router.push('/show/' + this.show_id.toString())
            }
        }

    }
</script>
<style>
    .show_title {
        text-align: center;
        margin-top: 12px;
    }

    .btn_pref {
        text-align: right;
        margin-top: 12px;

    }

    .is_in_pref {
        color: red
    }
</style>