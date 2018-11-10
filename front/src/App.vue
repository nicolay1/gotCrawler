<template>
    <div id="app">
        <notifications 
                    position="top right"
                    :speed="500"
                    :duration="10000"/>
        <router-view>

        </router-view>

    </div>
</template>

<script>

    export default {
        name: 'App',

    }
</script>

<style>
    #app {

    }
</style>