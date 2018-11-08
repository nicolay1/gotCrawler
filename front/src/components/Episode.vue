<template>
    <div class="card episode-card">
        <div class="container card-header">
            <div class="row episode-card-header">
                <div class="col-lg-2 col-md-6">
                    <img :src="pict">
                </div>
                <div class="col-lg-2 col-md-6 ep_number">
                    Episode n°{{ep_number}}
                </div>
                <div class="col-lg-7 col-md-6 title">
                    {{title}}
                </div>
                <div class="expand-icon toggle-button" v-b-toggle.ep_number>
                    <span class="expand-icon-text d-none d-sm-inline">Voir plus</span><font-awesome-icon  icon="angle-down" size="1x"/>
                </div>
            </div>
        </div>
        <b-collapse id="ep_number">
            <div class="card-body">
                <p>{{overview}}</p>
                <div class="separator"></div>
                <div>
                    <span class="toggle-button" v-b-toggle.crewList >Équipe technique <font-awesome-icon icon="angle-down" size="1x"/></span>
                    <span class="toggle-button" v-b-toggle.actorList >Liste des acteurs <font-awesome-icon icon="angle-down" size="1x"/></span>
                </div>
                <b-collapse class="crew-actor-collapse" id="crewList" >
                    <AuthorList :authors=authors />
                </b-collapse>
                <b-collapse class="crew-actor-collapse" id="actorList" >
                    <ActorList :actors=actors />
                </b-collapse>
            </div>
        </b-collapse>
    </div>

</template>

<script>
    import ActorList from './ActorList.vue'
    import AuthorList from './AuthorList.vue'

    export default {
        name: "Episode",
        components: {
            ActorList,
            AuthorList
        },
        props: {
            pict: String,
            ep_number: Number,
            title: String,
            overview: String,
            authors: Array,
            actors: Array,
        }
    }
</script>

<style scoped>

    .episode-card-header {
        text-align: center;
        position: relative;
    }
    .episode-card .expand-icon{
        position: absolute;
        bottom: calc(-1.25rem + 2px);
        right: calc(-.75rem + 2px);
    }
    .episode-card .expand-icon-text{
        position: relative;
        margin-right:5px;
    }
    .episode-card img{
        max-height: 100px;
    }
    .episode-card .separator{
        width: 100%;
        padding: 0;
        margin: 10px 0px;
        border-top: 1px solid rgba(0,0,0,.125);
        height: 0;
        margin-bottom: 15px;
    }
    .episode-card .toggle-button{
        background-color: #eee;
        cursor: pointer;
        padding: 5px;
        margin:5px;
    }
    .episode-card .crew-actor-collapse{
        margin-top:10px;
    }
</style>