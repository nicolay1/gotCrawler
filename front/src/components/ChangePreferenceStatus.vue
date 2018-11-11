<template>
    <b-btn v-on:click="ChangePref()">
        <font-awesome-icon :icon="['far', 'heart']" v-if="data_state===0"></font-awesome-icon>
        <font-awesome-icon :icon="['fas', 'heart']" v-else-if="data_state===1"></font-awesome-icon>
    </b-btn>

</template>

<script>

    import api from "../helpers/api.js"
    import User from "../helpers/user.js"

    export default {
        name: "ChangePreferenceStatus",
        props: {
            show_id: {type: Number, required: true},
            state: {type: Number},
        },
        data() {
            return {
                data_state: this.state,
                user: new User()
            }
        },
        methods: {
            ChangePref: function () {
                if (this.data_state === 0) {
                    api
                        .post('user/'+this.user.id+'/pref', {show_id: this.show_id})
                        .then(() => {
                            this.data_state = 1;
                            this.$parent.$parent.$emit('changestatus', [this.show_id, this.data_state]);


                        })
                        .catch((err) => console.log(err))

                }
                else if (this.data_state === 1) {
                    api
                        .delete('user/'+this.user.id+'/pref/'+this.show_id)
                        .then(() => {
                            this.data_state = 0;
                            this.$parent.$parent.$emit('changestatus', [this.show_id, this.data_state]);

                        })
                        .catch((err) => console.log(err))

                }
            }
        }

    }
</script>

<style scoped>

</style>