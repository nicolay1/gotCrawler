<template>
    <b-alert variant="primary" show dismissible v-on:dismissed="acknowledgeNotifications()"><p>L'épisode {{show.next_ep_num}} de la saison {{show.next_season_num}} de
        {{show.title}} sort le {{show.next_ep_date}}! Ne le manquez pas!</p></b-alert>
</template>

<script>
    import api from '../helpers/api.js'
    export default {

        name: "Notification",
        props: {
            show: {type: Object},
            user_id:{type:Number}
        },
        methods:{
            acknowledgeNotifications(){
                api.put("user/"+this.user_id+"/pref/"+this.show.id,{new_seen_flag:1}).then((res)=>this.$emit('notificationAcknowledged'))
            }
        }
    }

</script>

<style scoped>

</style>