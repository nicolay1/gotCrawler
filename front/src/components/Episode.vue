<template>
    <div class="card episode-card">
        <div class="card-header ">
            <div class="row episode-card-header">
            <span class="col-2 ep_number">
                Episode n°{{ep_number}}
            </span>
                <span class="col-2 pict">
                <img :src="pict">
            </span>
                <span class="col-7 title">
                {{title}}
            </span>
                <span class="col-1 expand-icon">
                <font-awesome-icon v-b-toggle="ep_number" icon="angle-down" size="2x"/>
            </span>
            </div>
        </div>

        <b-collapse :id="ep_number">
            <div class="card-body">
                {{overview}}
            </div>
        </b-collapse>
    </div>

</template>

<script>
    export default {
        name: "Episode",
        props: {
            pict: String,
            ep_number: String,
            title: String,
            overview: String,

        }
    }
</script>

<style scoped>

    .episode-card-header {
        text-align: center;

    }

    .ep_number {
        padding-top: 4%;
    }

    .title {
        padding-top: 4%;
    }
    .expand-icon{
        padding-top: 4%;
    }
</style>