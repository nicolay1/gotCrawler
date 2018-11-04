<template>
    <div class="container">
            <Episode
                    pict="https://cdn.kitten-things.com/wp-content/uploads/2017/03/introduce-kitten-older-cat-128x128.jpg"
                    title="GOT Ep5"
                    ep_number=5
                    overview="Quelquechose"></Episode>
        <Episode pict="https://cdn.kitten-things.com/wp-content/uploads/2017/03/introduce-kitten-older-cat-128x128.jpg"
                    title="GOT Ep6"
                    ep_number=6
                    overview="Quelquechose"></Episode>
    </div>
</template>
<script>
    import Episode from "./components/Episode.vue";

    export default {
        name: 'App',
        components: {
            Episode,
        }
    }
</script>