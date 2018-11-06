<template>
    <b-col cols="3" class="actor_card">
        <b-container class="card">
            <b-row align-v="center">
                <b-col md="12" lg="6" class="pict">
                    <b-img fluid class="img-thumbnail pict_class" :src="pict"/>
                </b-col>
                <b-col md="12" lg="6" align="Center" class="name">
                    {{name_actor}}
                </b-col>
            </b-row>
        </b-container>
    </b-col>
</template>
<script>
    export default {
        name: "Actor",
        props: {
            pict: String,
            name_actor: String,
        }
    }
</script>
<style scoped>
    .actor_card{
        padding: 2px 2px 2px 2px;
    }
    .pict{
        text-align: center;
        margin: 0px 0px 0px 0px;
        padding: 2px 2px 2px 2px;

    }
    .pict_class{
    max-height: 100px;


    }
    .name {
        text-align: center;

    }
</style>