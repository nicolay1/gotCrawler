<template>
    <div class="card" style="width: 18rem;">
        <div class="card-header">
            <button v-bind:class="{is_in_pref:state}" v-on:click="ChangePref()">
                {{message_button}}
            </button>
        </div>
        <img class="card-img-top" :src="pict" alt="Card image cap">

        <div class="card-body">
            <h5 class="card-title">{{title}}</h5>
            <p class="card-text">{{overview}}.</p>

            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        <div class="card-footer text-muted">
            {{date_to_string}}
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'ShowCard',
        props: {
            title: String,
            overview: String,
            pict: String,
            date_next_ep: Date,
            show_id: Number,
            state: {default: 0, type: Number}

        },
        data() {
            let date_to_string = this.date_next_ep.toLocaleDateString();

            let message_button="";
            if (this.state===0){
                message_button ="Ajouter dans les préférences"
            }
            else{
                 message_button="SuppriaddToPrefmer des préférences"
            }

            return {
                date_to_string: date_to_string,
                message_button : message_button,
                data_state:this.state
            }
        },
        methods: {
            ChangePref: function () {
                if (this.data_state === 0) {
                    axios
                        .post('http://localhost:5000/user/3/pref', {show_id: this.show_id})
                        .then(()=>{
                            this.message_button = "Supprimer des préférences";
                            this.data_state=1;
                        })
                        .catch((err)=>console.log(err))

                }
                else if (this.data_state === 1) {
                    axios
                        .delete('http://localhost:5000/user/3/pref', {data:{show_id: this.show_id}})
                        .then(()=>{
                            this.message_button = "Ajouter des préférences";
                            this.data_state=0;
                        })
                        .catch((err)=>console.log(err))

                }
            }
        }
    }
</script>
<style>
    .is_in_pref{
        color:red
    }
</style>