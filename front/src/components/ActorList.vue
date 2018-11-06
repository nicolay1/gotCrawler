<template>

    <b-container class="actor_class" fluid>
        <b-row class="actor_row">
            <Actor
                v-for="actor in actors"
                v-bind:pict="actor.pict"
                v-bind:name_actor="actor.name"
            >
            </Actor>
        </b-row>
    </b-container>


</template>
<script>
    import Actor from "./Actor.vue";
    export default {
        name: "ActorList",
        components: {
            Actor,
        },
        props: {
            actors: Array,
        }
    }
</script>
